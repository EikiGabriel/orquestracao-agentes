"""Lab 0.1: a primeira chamada nos 3 provedores.

Envia a MESMA pergunta para cada provedor configurado e mostra:
  - a resposta
  - por que o modelo parou de gerar
  - os tokens de entrada e de saída que o provedor informou

Uso:
    python labs/lab00_fundamentos/primeira_chamada.py
    python labs/lab00_fundamentos/primeira_chamada.py "Sua pergunta aqui"

Provedores sem chave ou sem modelo configurado são pulados (veja .env.example).
"""

import os
import sys

from dotenv import load_dotenv

load_dotenv()  # lê o .env se existir; no Codespaces os secrets já são env vars

PERGUNTA_PADRAO = "Explique o que é um token em LLMs em 2 frases."

# Preço do Claude Haiku 5.5 em US$ por milhão de tokens. É o preço "a partir de";
# prompts longos custam mais. Fonte: platform.claude.com/docs/models/overview
# (consultado em 09/11/2026). Confira antes de confiar no número.
HAIKU_PRECO_IN = 0.10
HAIKU_PRECO_OUT = 0.50


def chamar_anthropic(pergunta: str) -> dict:
    import anthropic

    client = anthropic.Anthropic()  # usa ANTHROPIC_API_KEY
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


def chamar_gemini(pergunta: str) -> dict:
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    model = os.environ["GEMINI_MODEL"]

    previa = client.models.count_tokens(model=model, contents=pergunta)
    resp = client.models.generate_content(model=model, contents=pergunta)

    uso = resp.usage_metadata
    return {
        "modelo": model,
        "texto": resp.text,
        "parada": resp.candidates[0].finish_reason if resp.candidates else None,
        "in_previsto": previa.total_tokens,
        "in": uso.prompt_token_count,
        "out": uso.candidates_token_count,
        "custo_usd": 0.0,  # tier gratuito (com rate limit baixo)
    }


def chamar_openai(pergunta: str) -> dict:
    from openai import OpenAI

    client = OpenAI()  # usa OPENAI_API_KEY
    model = os.environ["OPENAI_MODEL"]

    resp = client.responses.create(model=model, input=pergunta, max_output_tokens=2000)
    return {
        "modelo": model,
        "texto": resp.output_text,
        "parada": resp.status,  # "completed" ou "incomplete" (ex.: estourou max_output_tokens)
        "in_previsto": None,
        "in": resp.usage.input_tokens,
        "out": resp.usage.output_tokens,
        "custo_usd": None,  # depende de você estar no programa de data sharing
    }


PROVEDORES = {
    "anthropic": ("ANTHROPIC_API_KEY", "ANTHROPIC_MODEL", chamar_anthropic),
    "gemini": ("GEMINI_API_KEY", "GEMINI_MODEL", chamar_gemini),
    "openai": ("OPENAI_API_KEY", "OPENAI_MODEL", chamar_openai),
}


def main() -> None:
    pergunta = sys.argv[1] if len(sys.argv) > 1 else PERGUNTA_PADRAO
    print(f"Pergunta: {pergunta}\n")

    for nome, (env_chave, env_modelo, chamar) in PROVEDORES.items():
        if not os.getenv(env_chave) or not os.getenv(env_modelo):
            print(f"[{nome}] pulado: defina {env_chave} e {env_modelo}\n")
            continue
        try:
            r = chamar(pergunta)
        except Exception as e:  # num lab, queremos LER o erro, não esconder
            print(f"[{nome}] ERRO: {type(e).__name__}: {e}\n")
            continue

        print(f"[{nome}] {r['modelo']}")
        print(f"  resposta : {r['texto'].strip()}")
        print(f"  parada   : {r['parada']}")
        print(f"  tokens   : previsto={r['in_previsto']}  in={r['in']}  out={r['out']}")
        if r["custo_usd"] is not None:
            print(f"  custo    : US$ {r['custo_usd']:.6f}")
        print()


if __name__ == "__main__":
    main()
