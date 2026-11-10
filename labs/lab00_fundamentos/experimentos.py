"""Lab 0.1: experimentos.

Experimento A (idioma): conta os tokens do mesmo texto em PT e em EN.
Usa count_tokens, que só conta e não gera resposta (custo zero).

Uso:
    python labs/lab00_fundamentos/experimentos.py
"""

import os

import anthropic

from primeira_chamada import chave_api  # também carrega o .env

client = anthropic.Anthropic(api_key=chave_api())
MODEL = os.environ["ANTHROPIC_MODEL"]

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


if __name__ == "__main__":
    experimento_a()
