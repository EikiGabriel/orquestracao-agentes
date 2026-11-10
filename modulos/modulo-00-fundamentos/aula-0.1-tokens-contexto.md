# Aula 0.1: tokens, janela de contexto e a API stateless

**Tema:** tokens, janela de contexto e a API "sem memória" · **Data:** 09/11/2026

## Conceitos
- **Token:** a unidade de texto que o modelo lê e escreve (um pedaço de palavra). Você paga pelos tokens de entrada e de saída; **a saída é bem mais cara** (~5x no Claude).
- **Janela de contexto, a analogia da mesa:** o modelo só enxerga o que está "em cima da mesa" naquela chamada. **A cada chamada a mesa começa vazia.** Para ele "lembrar", você reenvia o histórico inteiro.
- **Consequência:** numa conversa longa, **cada turno custa mais que o anterior**, porque o histórico é reenviado sempre.
- **Sampling:** o modelo calcula uma distribuição de probabilidades e sorteia o próximo token. A *temperature* achatava ou afiava essa distribuição.

```
Cada chamada à API (stateless: a mesa começa vazia)
┌──────────────────────────────────────────────────┐
│ ENTRADA  (input tokens)                          │
│   ├─ system prompt                               │
│   ├─ definições de ferramentas                   │
│   ├─ histórico: user → assistant → user → ...    │ ← VOCÊ reenvia tudo, sempre
│   └─ mensagem nova                               │
├──────────────────────────────────────────────────┤
│ SAÍDA    (output tokens, cerca de 5x mais caros) │
│   ├─ thinking (raciocínio)                       │ ← conta no max_tokens
│   └─ texto  ou  pedido de ferramenta (tool_use)  │
└──────────────────────────────────────────────────┘
        entrada + saída ≤ janela de contexto
```

## Estado da arte (pesquisado em 09/11/2026)
**(a) Consenso**
- Modelos atuais da Anthropic (doc oficial): Fable 5.1 (US$10/US$50 por MTok), Opus 5.5 (US$4/US$20), Sonnet 5.5 (US$2/US$10), **Haiku 5.5 (a partir de US$0,10/US$0,50)**. Todos com janela de **1M tokens** e saída máxima de **128K**. No Haiku 5.5, prompts longos custam mais.
- Existe um endpoint de **contagem de tokens** (`messages.count_tokens`) que aceita a mesma entrada de uma mensagem e devolve os tokens de entrada antes do envio.

**(b) Tendência recente**
- **O botão de temperature saiu dos modelos de ponta.** Nos Claude 5.5, `temperature`, `top_p` e `top_k` devem ser omitidos (erro 400). A OpenAI fez o mesmo nos modelos de raciocínio GPT-5 (só aceitam `temperature=1`). Mesmo antes, `temperature=0` nunca garantiu saídas idênticas.
- **O novo controle é o `effort`** (`output_config.effort`), com **thinking adaptativo** ligado por padrão.
- **O raciocínio consome o `max_tokens`:** um teto baixo pode parar com `stop_reason: "max_tokens"` antes de sair qualquer texto.
- **O tokenizer mudou:** a partir do Claude Opus 4.7, o mesmo texto conta ~30% mais tokens. Não compare contagens entre modelos ou provedores.

**(c) Cuidado com o marketing**
- "1M de contexto" não significa "jogue tudo lá dentro": o contexto efetivamente útil é menor que a janela nominal (tema do Módulo 3).

## Código mínimo (Anthropic SDK)
```python
import anthropic

client = anthropic.Anthropic()          # lê ANTHROPIC_API_KEY do ambiente (ver nota abaixo)
MODEL = "claude-haiku-5-5"
messages = [{"role": "user", "content": "Explique o que é um token em 2 frases."}]

contagem = client.messages.count_tokens(model=MODEL, messages=messages)
print("Tokens de entrada (estimativa):", contagem.input_tokens)

# sem temperature: dá erro 400 nos modelos 5.5
resp = client.messages.create(model=MODEL, max_tokens=2000, messages=messages)

texto = "".join(b.text for b in resp.content if b.type == "text")  # filtrar por TIPO
print(texto)
print("stop_reason:", resp.stop_reason)
print("uso:", resp.usage.input_tokens, "in /", resp.usage.output_tokens, "out")
```

> **Nota (v1.1):** nas sessões do Claude Code na nuvem, `ANTHROPIC_API_KEY` não chega ao script. Lá a chave fica em `LAB_ANTHROPIC_API_KEY` e é passada explicitamente: `anthropic.Anthropic(api_key=chave_api())`, como em `labs/lab00_fundamentos/primeira_chamada.py`.

## Armadilhas
- Achar que o modelo lembra (a memória é sempre o histórico que você reenvia).
- Ler `resp.content[0].text`: pode ser um bloco de thinking.
- `max_tokens` apertado num modelo que raciocina: a resposta vem cortada ou vazia.
- Confiar em `temperature=0` para ter determinismo; para saídas estáveis, use *structured outputs*.
- Comparar tokens entre modelos ou provedores (tokenizers diferentes).
- Vazar a API key no GitHub.

## Perguntas de fixação
1. Se a API é stateless, como o Claude Code "lembra" do que você fez 20 minutos atrás? O que acontece com o custo de cada turno à medida que a sessão cresce?
2. Por que o idioma dos prompts importa num sistema com 7 agentes trocando mensagens o tempo todo?
3. Como garantir que o Agente Revisor responda só "aprovar", "pedir mudanças" ou "escalar", sem usar temperature? (ponte para a Aula 0.2)

**Laboratório:** [Lab 0.1](../../labs/lab00_fundamentos/README.md)

---
Fonte: [GUIA_DE_ESTUDO.md, seção 10](../../docs/GUIA_DE_ESTUDO.md#10-notas-da-aula-01) (v1.1).
