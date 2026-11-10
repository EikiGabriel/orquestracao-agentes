"""Lab 0.1: experimentos.

A (idioma): conta os tokens do mesmo texto em PT e em EN.
   Usa count_tokens, que só conta e não gera resposta (custo zero).
B (stateless): conta um fato ao modelo e pergunta por ele numa chamada
   nova, primeiro sem e depois com o histórico.
C (corte): pede uma explicação longa com max_tokens=50.

Uso:
    python labs/lab00_fundamentos/experimentos.py          # roda A, B e C
    python labs/lab00_fundamentos/experimentos.py b c      # só os escolhidos
"""

import os
import sys

import anthropic

# primeira_chamada também carrega o .env
from primeira_chamada import HAIKU_PRECO_IN, HAIKU_PRECO_OUT, chave_api

client = anthropic.Anthropic(api_key=chave_api())
MODEL = os.environ["ANTHROPIC_MODEL"]

custo_total = 0.0  # soma das chamadas que geram resposta (B e C)

# Dante, Inferno, Canto I (a loba). Tradução portuguesa antiga.
TEXTO_PT = """Que me investisse então cuido inquieto;
Com fome e raiva atroz fronte levanta;
Tremer parece o ar ao seu conspeto.

Eis surge loba, que de magra espanta;
De ambições todas parecia cheia;
Foi causa a muitos de miséria tanta!

Com tanta intensa torvação me enleia
Pelo terror, que o cenho seu movia,
Que a mente à altura não subir receia.

Como quem lucro anela noite e dia,
Se acaso o tempo de perder lhe chega,
Rebenta em pranto e triste se excrucia,

A fera assim me fez, que não sossega;
Pouco a pouco me investe até lançar-me
Lá onde o sol se cala e a luz me nega."""

# Tradução fiel do texto acima, verso a verso.
TEXTO_EN = """I thought, uneasy, it was charging at me then;
With hunger and fierce rage it raised its brow;
The very air seemed to tremble in its presence.

Then a she-wolf appears, frightening in her leanness;
She seemed full of every craving;
She brought such misery to so many!

With such intense dread she entangles me
Through the terror that her brow stirred,
That my mind fears to climb to the height.

Like one who longs for gain night and day,
If by chance the time comes for him to lose,
Bursts into tears and sadly torments himself,

So the beast made me, never resting;
Little by little she presses on me until she throws me
Back to where the sun falls silent and the light is denied me."""


def contar(texto: str) -> int:
    """Tokens de entrada de uma mensagem com esse texto."""
    r = client.messages.count_tokens(
        model=MODEL, messages=[{"role": "user", "content": texto}]
    )
    return r.input_tokens


def experimento_a() -> None:
    sobra = contar("a")  # tokens fixos da estrutura da mensagem (+1 do "a")
    pt, en = contar(TEXTO_PT), contar(TEXTO_EN)
    pal_pt, pal_en = len(TEXTO_PT.split()), len(TEXTO_EN.split())

    print("== Experimento A: idioma ==")
    print(f"sobra fixa da mensagem: ~{sobra} tokens")
    print(f"PT: {pt} tokens  {pal_pt} palavras  {pt / pal_pt:.2f} tokens/palavra")
    print(f"EN: {en} tokens  {pal_en} palavras  {en / pal_en:.2f} tokens/palavra")
    print(f"razão PT/EN (bruta):     {pt / en:.2f}")
    print(f"razão PT/EN (sem sobra): {(pt - sobra) / (en - sobra):.2f}")


def chamar(messages: list, max_tokens: int = 500):
    """Uma chamada ao modelo; soma o custo em custo_total."""
    global custo_total
    # Sem temperature: os modelos Claude 5.5 rejeitam esse parâmetro (erro 400)
    resp = client.messages.create(model=MODEL, max_tokens=max_tokens, messages=messages)
    custo_total += (
        resp.usage.input_tokens * HAIKU_PRECO_IN
        + resp.usage.output_tokens * HAIKU_PRECO_OUT
    ) / 1_000_000
    return resp


def texto(resp) -> str:
    # Filtra pelo tipo do bloco; nunca use resp.content[0] (pode ser 'thinking')
    return "".join(b.text for b in resp.content if b.type == "text").strip()


def mostrar(rotulo: str, resp) -> None:
    print(f"[{rotulo}]")
    print(f"  resposta : {texto(resp) or '(nenhum texto)'}")
    print(f"  parada   : {resp.stop_reason}")
    print(f"  tokens   : in={resp.usage.input_tokens}  out={resp.usage.output_tokens}")
    print(f"  blocos   : {[b.type for b in resp.content]}")


def experimento_b() -> None:
    print("\n== Experimento B: stateless ==")
    fato = {"role": "user", "content": "Meu número favorito é 42."}
    pergunta = {"role": "user", "content": "Qual é meu número favorito?"}

    r1 = chamar([fato])
    mostrar("chamada 1: conta o fato", r1)

    # Chamada nova, só com a pergunta: a API não guarda nada da chamada 1
    r2 = chamar([pergunta])
    mostrar("chamada 2: sem histórico", r2)

    # Agora reenviando o histórico completo: user -> assistant -> user
    historico = [fato, {"role": "assistant", "content": texto(r1)}, pergunta]
    r3 = chamar(historico)
    mostrar("chamada 2: com histórico", r3)


def experimento_c() -> None:
    print("\n== Experimento C: corte com max_tokens=50 ==")
    pedido = (
        "Explique em detalhes como funciona a arquitetura Transformer: "
        "embeddings, atenção, camadas feed-forward e geração de texto."
    )
    r = chamar([{"role": "user", "content": pedido}], max_tokens=50)
    mostrar("max_tokens=50", r)
    print(f"  veio texto? {'sim' if texto(r) else 'não'}")


EXPERIMENTOS = {"a": experimento_a, "b": experimento_b, "c": experimento_c}


if __name__ == "__main__":
    escolhidos = [a.lower() for a in sys.argv[1:]] or list(EXPERIMENTOS)
    invalidos = [n for n in escolhidos if n not in EXPERIMENTOS]
    if invalidos:
        sys.exit(f"Experimentos inválidos: {invalidos}. Use: {', '.join(EXPERIMENTOS)}")
    for nome in escolhidos:
        EXPERIMENTOS[nome]()
    print(f"\ncusto estimado desta execução: US$ {custo_total:.6f}")
