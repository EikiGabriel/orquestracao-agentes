"""Lab 0.1: a primeira chamada ao Claude Haiku.

Envia uma pergunta ao Claude e mostra:
  - a resposta
  - por que o modelo parou de gerar
  - os tokens de entrada (previstos e cobrados) e de saída
  - o custo estimado da chamada

Uso:
    python labs/lab00_fundamentos/primeira_chamada.py
    python labs/lab00_fundamentos/primeira_chamada.py "Sua pergunta aqui"

Precisa de ANTHROPIC_MODEL e da chave em LAB_ANTHROPIC_API_KEY ou
ANTHROPIC_API_KEY (veja .env.example).
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()  # lê o .env se existir; variáveis de ambiente já definidas têm prioridade

PERGUNTA_PADRAO = "Explique o que é um token em LLMs em 2 frases."

# Preço do Claude Haiku 5.5 em US$ por milhão de tokens. É o preço "a partir de";
# prompts longos custam mais. Fonte: platform.claude.com/docs/models/overview
# (consultado em 09/11/2026). Confira antes de confiar no número.
HAIKU_PRECO_IN = 0.10
HAIKU_PRECO_OUT = 0.50


def chave_api() -> str | None:
    # LAB_ANTHROPIC_API_KEY vem primeiro: nas sessões do Claude Code na nuvem,
    # a variável ANTHROPIC_API_KEY não chega ao script.
    return os.getenv("LAB_ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_API_KEY")


def chamar_claude(pergunta: str) -> dict:
    import anthropic

    client = anthropic.Anthropic(api_key=chave_api())
    model = os.environ["ANTHROPIC_MODEL"]
    messages = [{"role": "user", "content": pergunta}]

    # Contagem ANTES de enviar: endpoint próprio, não gera resposta
    previa = client.messages.count_tokens(model=model, messages=messages)

    # Sem temperature: os modelos Claude 5.5 rejeitam esse parâmetro (erro 400)
    resp = client.messages.create(model=model, max_tokens=2000, messages=messages)

    # A resposta é uma LISTA de blocos (pode ter 'thinking' antes do 'text').
    # Filtre pelo tipo; nunca use resp.content[0].
    texto = "".join(b.text for b in resp.content if b.type == "text")
    custo = (
        resp.usage.input_tokens * HAIKU_PRECO_IN
        + resp.usage.output_tokens * HAIKU_PRECO_OUT
    ) / 1_000_000
    return {
        "modelo": model,
        "texto": texto,
        "parada": resp.stop_reason,
        "in_previsto": previa.input_tokens,
        "in": resp.usage.input_tokens,
        "out": resp.usage.output_tokens,
        "custo_usd": custo if "haiku" in model else None,
    }


def main() -> None:
    pergunta = sys.argv[1] if len(sys.argv) > 1 else PERGUNTA_PADRAO
    print(f"Pergunta: {pergunta}\n")

    faltando = []
    if not chave_api():
        faltando.append("LAB_ANTHROPIC_API_KEY (ou ANTHROPIC_API_KEY)")
    if not os.getenv("ANTHROPIC_MODEL"):
        faltando.append("ANTHROPIC_MODEL")
    if faltando:
        sys.exit(f"Defina {' e '.join(faltando)} (veja .env.example).")

    try:
        r = chamar_claude(pergunta)
    except Exception as e:  # num lab, queremos LER o erro, não esconder
        sys.exit(f"ERRO: {type(e).__name__}: {e}")

    print(f"[{r['modelo']}]")
    print(f"  resposta : {r['texto'].strip()}")
    print(f"  parada   : {r['parada']}")
    print(f"  tokens   : previsto={r['in_previsto']}  in={r['in']}  out={r['out']}")
    if r["custo_usd"] is not None:
        print(f"  custo    : US$ {r['custo_usd']:.6f}")


if __name__ == "__main__":
    main()
