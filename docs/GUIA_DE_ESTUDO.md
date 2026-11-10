# Guia de Estudo: Orquestração de Agentes de IA

> Documento-base do repositório `EikiGabriel/orquestracao-agentes`.
> Consolida o plano de estudo, o sistema-alvo, o currículo, os laboratórios, as decisões já tomadas e o conteúdo da primeira aula.
> **Versão:** 1.1 · **Data:** 10/11/2026 · **Status:** Módulo 0 em andamento (Aula 0.1 dada; Lab 0.1: execução base ok no Claude Haiku 5.5, experimentos em andamento)

| Versão | Data | Mudanças |
|---|---|---|
| 1.0 | 10/11/2026 | Primeira versão do guia. |
| 1.1 | 10/11/2026 | Só o Claude Haiku 5.5 como provedor (Gemini e OpenAI saem do estudo); chave em `LAB_ANTHROPIC_API_KEY` nas sessões do Claude Code na nuvem; critério de pronto do Lab 0.1 ajustado; repositório estruturado a partir deste guia. |

---

## Sumário
1. [Objetivo do estudo](#1-objetivo-do-estudo)
2. [O sistema-alvo](#2-o-sistema-alvo)
3. [Humano no loop (HITL)](#3-humano-no-loop-hitl)
4. [Perfil, ambiente e decisões](#4-perfil-ambiente-e-decisões)
5. [Cronograma](#5-cronograma)
6. [Currículo por módulo](#6-currículo-por-módulo)
7. [Laboratórios](#7-laboratórios)
8. [Formato de cada aula](#8-formato-de-cada-aula)
9. [Regras de pesquisa e de fontes](#9-regras-de-pesquisa-e-de-fontes)
10. [Notas da Aula 0.1](#10-notas-da-aula-01)
11. [Glossário](#11-glossário)
12. [Fontes consultadas](#12-fontes-consultadas)
13. [Anexo: instruções para o Claude Code](#13-anexo-instruções-para-o-claude-code)

---

## 1. Objetivo do estudo
Aprender **orquestração de agentes de IA** dos fundamentos à prática e, ao final, ter **um sistema multiagente funcional para desenvolvimento de software, com humano no loop**, rodando sobre este repositório.

Princípios do estudo:
- **A solução mais simples que funcione.** Complexidade só entra com justificativa.
- **Aprender fazendo.** Cada módulo termina com um laboratório que tem critério de "pronto".
- **Honestidade sobre limitações e hype.** Separar consenso, tendência e marketing.
- **Pesquisa atualizada.** Tudo o que muda rápido é verificado em fonte primária antes de ser ensinado.

---

## 2. O sistema-alvo
Um **orquestrador** distribui o trabalho entre agentes especializados. Ele é o fio condutor de todo o estudo: cada módulo constrói uma peça dele.

```
                         ┌────────────────────┐
           tarefa/spec → │    ORQUESTRADOR    │ ← estado do projeto
                         └─────────┬──────────┘
        ┌──────────┬───────────┬───┴───────┬────────────┬────────────┐
        ▼          ▼           ▼           ▼            ▼            ▼
  Desenvolvedor  Revisor   Guardrails  Boas Práticas  Otimização  Contexto/Memória
        └──────────┴───────────┴───────────┴────────────┴────────────┘
                                   │
                        Assistente Administrativo
                  (decisões, backlog, log, documentação viva)
                                   │
                          HUMANO (só quando necessário)
```

| # | Agente | Responsabilidade | Módulos onde nasce |
|---|---|---|---|
| 1 | **Desenvolvedor** | Escreve código a partir de tarefas/specs | 1, 2 |
| 2 | **Revisor** | Revisa bugs, legibilidade e aderência à spec | 2 |
| 3 | **Guardrails** | Segurança: segredos expostos, prompt injection, permissões de ferramentas, políticas | 6 |
| 4 | **Boas Práticas** | Padrões de arquitetura, testes, convenções do projeto | 2, 3 |
| 5 | **Otimização** | Performance, custo (tokens, latência), simplificação | 9 |
| 6 | **Contexto/Memória** | Decide o que cada agente precisa saber; resume, compacta e repassa contexto entre etapas (context engineering) | 3 |
| 7 | **Assistente Administrativo** | Mantém o estado do projeto: decisões, backlog, pendências, log de execuções, documentação viva | 3, 10 |

**Ideia central (da Aula 0.1):** a API de um LLM é *stateless*. Nada passa de um agente para outro sozinho. Alguém precisa decidir o que vai para o contexto de cada agente, e esse é o papel do Agente de Contexto/Memória.

---

## 3. Humano no loop (HITL)
O humano **só é acionado quando necessário**:
- Aprovar ou revisar **Pull Requests** antes do merge.
- Quando a **confiança** do agente estiver abaixo de um limiar definido.
- Quando **faltar contexto** ou houver **requisito ambíguo**.
- Antes de **ações irreversíveis ou de alto risco** (deploy, apagar dados, gastar acima do orçamento).
- Quando o agente **não tiver certeza** de algo.

**Formato obrigatório de todo acionamento:**
```
O QUE FOI FEITO:   resumo curto do trabalho até aqui
DÚVIDA EXATA:      a pergunta que só o humano pode responder
OPÇÕES:            A) ...  B) ...  C) ...
RECOMENDAÇÃO:      opção X, porque ...
```

> Este repositório já pratica o fluxo: o agente propõe (branch + PR) e o humano revisa e faz o merge.

---

## 4. Perfil, ambiente e decisões

### 4.1 Perfil (diagnóstico de 09/11/2026)
| Item | Situação |
|---|---|
| Programação | Python (3 anos) + SQL |
| LLMs | Nível 1: chat e chamadas simples de API. Tool calling ainda não usado; LangChain e CrewAI usados muito pouco. **Começar do zero.** |
| Tempo | ~1h por dia (≈ 5–7h/semana) |
| Ferramentas | GitHub, Claude Code, chaves de API da Anthropic, OpenAI e Gemini |
| Restrição | Computador da empresa, onde `git clone`/`git push` para projetos externos não funcionam |
| Ponto a reforçar | Tool use: o modelo **não executa e nem chama** a ferramenta. Ele **gera um pedido estruturado** (nome + argumentos JSON) e **o código da aplicação executa** e devolve o resultado. MCP é um **protocolo** para expor ferramentas, não uma ferramenta. |

### 4.2 Registro de decisões
| Data | Decisão | Motivo |
|---|---|---|
| 09/11/2026 | Labs em **Python** | Linguagem dominada |
| 09/11/2026 | **Claude Haiku 5.5** (`claude-haiku-5-5`) como modelo pago padrão | O mais barato da linha atual da Anthropic |
| 09/11/2026 | Ler a resposta da API **pelo `type` dos blocos**, nunca por posição | A resposta pode começar com blocos `thinking` |
| 09/11/2026 | **Não usar `temperature`/`top_p`/`top_k`** nos modelos Claude 5.5 | Retornam erro 400; o comportamento se guia pelo prompt e pelo `effort` |
| 09/11/2026 | Orçamento de **US$10/mês** em API paga, usando antes os tiers gratuitos | Custo de estudo controlado |
| 09/11/2026 | Wrapper próprio e fino entre provedores (`llm.py`) a partir do Lab 2; **nenhum framework antes do Módulo 5** | Entender o mecanismo antes da abstração. *A reavaliar (10/11/2026): com um só provedor, o wrapper pode não ser necessário.* |
| 10/11/2026 | Repositório **privado** `EikiGabriel/orquestracao-agentes`; tudo entra por **PR** | Versionamento + prática de HITL |
| 10/11/2026 | Execução no **GitHub Codespaces** com devcontainer; chaves como *Codespaces secrets* | Contorna as restrições do computador da empresa |
| 10/11/2026 | Usar **só o Claude Haiku 5.5**; Gemini e OpenAI saem do estudo (PR #2) | Simplificar: um provedor, um SDK, uma chave |
| 10/11/2026 | **Não versionar o `.env`**; o `.env.example` continua como modelo sem segredos | Uma chave commitada fica no histórico do git para sempre |
| 10/11/2026 | Nas sessões do **Claude Code na nuvem**, a chave fica em `LAB_ANTHROPIC_API_KEY` (PR #3, issue #4) | Lá a variável `ANTHROPIC_API_KEY` não chega ao script; o código lê `LAB_ANTHROPIC_API_KEY` e, se não existir, `ANTHROPIC_API_KEY` |

### 4.3 Estratégia de modelos e orçamento
**Desde 10/11/2026 o estudo usa só o Claude Haiku 5.5.** As linhas de Gemini e OpenAI ficam como registro histórico.

| Uso | Provedor | Observações |
|---|---|---|
| Todos os labs: chamadas simples, experimentos, loops de agente e multiagente | **Claude Haiku 5.5 (pago)** | A partir de US$0,10 / US$0,50 por milhão de tokens (in/out). Um lab custa centavos: a primeira chamada do Lab 0.1 custou US$ 0,000062. |
| ~~Chamadas simples, experimentos, avaliação em lote~~ | ~~Gemini, tier gratuito (Flash-Lite)~~ | **Fora do estudo desde 10/11/2026.** Limites baixos e definidos por projeto; os dados podem ser usados pelo Google. |
| ~~Comparação entre provedores (Módulo 9)~~ | ~~Os 3~~ | **Fora do estudo desde 10/11/2026.** O Módulo 9 compara modelos da Anthropic entre si. |
| ~~Opcional~~ | ~~OpenAI, tokens de data sharing~~ | **Fora do estudo desde 10/11/2026.** |

### 4.4 Regras do repositório
1. **Nenhuma chave de API no código ou nos commits.** O `.env` fica no `.gitignore`; no Codespaces, use secrets; nas sessões do Claude Code na nuvem, cadastre a chave como `LAB_ANTHROPIC_API_KEY` nas variáveis do ambiente. Padronizar um nome único é a issue #5.
2. **Nada de código ou dados da empresa**, sobretudo em tiers gratuitos (que treinam com os dados enviados).
3. **Tudo entra por Pull Request**, com descrição, critério de pronto e limitações conhecidas.
4. Pendência: confirmar a política da empresa sobre projeto pessoal no computador de trabalho.

---

## 5. Cronograma
**≈16 semanas, 1h por dia.** Ritmo semanal: **Seg/Ter** conceito · **Qua/Qui** laboratório · **Sex** revisão + diário.

| Semana | Módulo | Laboratório | Peça do sistema-alvo |
|---|---|---|---|
| 1 | 0: Fundamentos de LLMs | Lab 0.1 | — |
| 2 | 1: Do prompt ao agente | Lab 1 | Desenvolvedor (versão 0) |
| 3–4 | 2: Padrões de orquestração | Labs 2 e 3 | Orquestrador, Revisor, Boas Práticas |
| 5–6 | 3: Context engineering e memória | Lab 4 | Contexto/Memória, Administrativo |
| 7 | 4: Protocolos (MCP, A2A) | — | Ferramentas via MCP |
| 8 | 5: Frameworks e SDKs | spike comparativo | Escolha do framework do projeto |
| 9 | 6: Guardrails e segurança | Lab 5 | Guardrails |
| 10 | 7: Human-in-the-loop | Lab 6 | Fluxo de aprovação via PR |
| 11 | 8: Avaliação e observabilidade | Lab 7 | Evals + tracing |
| 12 | 9: Otimização | Lab 8 | Otimização |
| 13–16 | 10: Projeto final | sistema completo | Tudo integrado |

---

## 6. Currículo por módulo

### Módulo 0: Fundamentos de LLMs (semana 1)
**Objetivo:** entender o que entra e sai de uma chamada a um LLM, quanto custa e quais são os limites.
- **Aula 0.1: tokens, janela de contexto, API stateless, sampling/temperature, `max_tokens`** ✅ (notas na seção 10)
- **Aula 0.2: tool use / function calling e structured outputs.** O ciclo "o modelo pede → o código executa → devolve o resultado", implementado à mão; saídas com schema (por exemplo, enum para vereditos).
- **Aula 0.3: raciocínio (thinking adaptativo, `effort`), limitações (alucinação, viés) e custo.**

### Módulo 1: Do prompt ao agente (semana 2)
- O loop de agente: **pensar → agir → observar**, até uma condição de parada.
- Ferramentas: definição, descrição, validação de argumentos, tratamento de erro.
- **Workflows vs. agentes:** quando NÃO usar um agente (fluxo fixo é mais barato, previsível e testável).
- Limites de segurança do loop: máximo de iterações, orçamento de tokens, timeouts.

### Módulo 2: Padrões de orquestração (semanas 3–4)
Padrões e os trade-offs de **custo, latência e falhas** de cada um:
- Orquestrador-workers
- Pipeline sequencial
- Roteador/triagem
- Fan-out/fan-in (paralelismo)
- Hierárquico/supervisor
- Debate / avaliador-otimizador
- Peer-to-peer

### Módulo 3: Context engineering e memória (semanas 5–6)
- Passagem de contexto entre agentes; como evitar o "telefone sem fio".
- Compactação e resumos; memória de curto e de longo prazo.
- RAG; estado compartilhado.
- Janela grande ≠ atenção boa: o contexto efetivo degrada com o tamanho.

### Módulo 4: Protocolos e interoperabilidade (semana 7)
- **MCP** (agente ↔ ferramentas/dados) e **A2A** (agente ↔ agente), além de protocolos que surgirem.
- Segurança de servidores MCP.

### Módulo 5: Frameworks e SDKs (semana 8)
Comparar, com pesquisa atualizada: Claude Agent SDK, OpenAI Agents SDK, LangGraph, CrewAI, Google ADK, Microsoft Agent Framework, Pydantic AI etc.
**Critérios:** controle de fluxo, estado/checkpoint, HITL nativo, observabilidade, lock-in.
**Saída:** decisão registrada sobre o framework do projeto final (ou "sem framework", se o wrapper próprio bastar).

### Módulo 6: Guardrails e segurança (semana 9)
- Prompt injection direta e indireta (via arquivos, issues, páginas web).
- Validação de entrada e de saída; sandboxing.
- Menor privilégio para ferramentas; red teaming.

### Módulo 7: Human-in-the-loop (semana 10)
- Pontos de aprovação, limiares de confiança, escalonamento.
- UX da intervenção humana (o formato da seção 3).
- Integração com PRs no GitHub.

### Módulo 8: Avaliação e observabilidade (semana 11)
- Evals de agentes; LLM-as-judge.
- Tracing (OpenTelemetry); métricas de custo e qualidade.
- Testes de regressão de prompts.

### Módulo 9: Otimização (semana 12)
- Escolha de modelo por tarefa (grande x pequeno, e entre provedores).
- Prompt caching, paralelismo, redução de tokens.
- Quando multiagente custa mais do que vale.

### Módulo 10: Projeto final (semanas 13–16)
Montar, testar e iterar o sistema completo da seção 2 sobre este repositório.

---

## 7. Laboratórios
Cada lab fica em `labs/labNN_nome/` com `README.md` (roteiro), código e `RESULTADOS.md` (entrega), e entra no repositório por PR.

> Os critérios dos Labs 1–8 são **preliminares**: serão detalhados quando a aula correspondente for dada.

### Lab 0.1: Tokens, janela de contexto e a API stateless (em andamento)
**Base:** `labs/lab00_fundamentos/primeira_chamada.py` manda uma pergunta ao Claude Haiku 5.5 e mostra a resposta, o motivo de parada, os tokens e o custo. Entrou no PR #1 com 3 provedores e foi simplificado para só o Claude no PR #2. ✅ Rodou de verdade em 10/11/2026.
**Experimentos (código escrito pela estudante):**
- **A. Idioma:** um parágrafo de ~100 palavras em PT e em EN; contar os tokens no Claude; calcular a razão PT/EN.
- **B. Stateless:** "Meu número favorito é 42" → nova chamada sem histórico ("Qual é meu número favorito?") → repetir com o histórico completo.
- **C. Corte:** `max_tokens=50` numa explicação longa; observar o `stop_reason` e se veio texto.
- **Bônus:** `temperature=0` no Claude; ler o erro.

**Pronto quando:** o script roda no Claude Haiku 5.5, `RESULTADOS.md` está preenchido (tabela PT/EN, explicação do stateless, `stop_reason`, custo estimado, as 3 perguntas de fixação) e foi entregue por PR.

### Lab 1: Um agente com 1 ferramenta
Loop de agente escrito à mão (sem framework) com uma ferramenta simples (por exemplo, `ler_arquivo` ou uma calculadora).
**Pronto quando:** o loop termina sozinho; tem limite de iterações; registra cada passo (pensamento, chamada, resultado); trata uma ferramenta que falha sem quebrar.

### Lab 2: Pipeline Dev → Revisor
O Agente Desenvolvedor gera código a partir de uma spec; o Revisor devolve uma **saída estruturada** (`veredito` ∈ {aprovar, pedir_mudancas, escalar} + lista de problemas); até N rodadas.
**Pronto quando:** o pipeline converge ou escala; registra rodadas, tokens e custo por execução; o `llm.py` (wrapper entre provedores) está criado.

### Lab 3: Orquestrador com roteamento para 3 agentes
Um roteador classifica a tarefa (structured output) e despacha para Desenvolvedor, Revisor ou Boas Práticas.
**Pronto quando:** um conjunto de ~10 tarefas de teste é roteado corretamente em ≥ 9/10, com log das decisões.

### Lab 4: Agente de Contexto passando resumos entre etapas
Um agente que resume e repassa só o necessário entre as etapas.
**Pronto quando:** existe medição de tokens antes/depois da compactação e um teste de "telefone sem fio" (um fato crítico precisa chegar intacto ao fim da cadeia).

### Lab 5: Guardrails + teste de prompt injection
Detecção de segredos, allowlist de ferramentas e defesa contra injection indireta (por exemplo, instrução maliciosa escondida num arquivo do repo).
**Pronto quando:** existe uma suíte de ataques com a taxa de bloqueio medida e documentada.

### Lab 6: HITL — abrir PR no GitHub e pausar até a aprovação
O sistema abre um PR e **pausa** até a aprovação humana; acionamentos no formato da seção 3.
**Pronto quando:** o fluxo completo (PR → pausa → aprovação/recusa → continuação) funciona e fica registrado.

### Lab 7: Evals e tracing do sistema
Dataset de tarefas, LLM-as-judge e traces (OpenTelemetry).
**Pronto quando:** existe um relatório de regressão comparando duas versões do sistema.

### Lab 8: Otimização de custo e latência
Baseline vs. mudanças (modelo menor, caching, paralelismo).
**Pronto quando:** existe uma tabela antes/depois de custo, latência e qualidade, com uma conclusão.

---

## 8. Formato de cada aula
1. Objetivo da aula (1–2 frases).
2. Conceito explicado com analogia + diagrama (quando ajudar).
3. Estado da arte (pesquisado, com datas e fontes).
4. Exemplo de código mínimo e funcional, comentado.
5. Laboratório prático, com critério de "pronto".
6. Armadilhas comuns e modos de falha.
7. 3 perguntas de fixação.
8. Próximo passo sugerido.

---

## 9. Regras de pesquisa e de fontes
- Antes de ensinar algo que muda rápido (frameworks, protocolos, modelos, benchmarks, boas práticas, papers): **pesquisar na web**.
- Priorizar **fontes primárias**: documentação oficial, blogs de engenharia (Anthropic, OpenAI, Google, Microsoft, LangChain), arXiv, repositórios e especificações oficiais (MCP, A2A).
- Sempre informar a **data da fonte** e a **versão** do framework/SDK; **sinalizar quando tiver mais de 6 meses**.
- Separar: **(a)** consenso consolidado · **(b)** tendência emergente · **(c)** opinião/marketing.
- Nunca inventar APIs, parâmetros ou resultados.
- Toda resposta baseada em pesquisa termina com **"Fontes:"**.

---

## 10. Notas da Aula 0.1
**Tema:** tokens, janela de contexto e a API "sem memória" · **Data:** 09/11/2026

### Conceitos
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

### Estado da arte (pesquisado em 09/11/2026)
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

### Código mínimo (Anthropic SDK)
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

### Armadilhas
- Achar que o modelo lembra (a memória é sempre o histórico que você reenvia).
- Ler `resp.content[0].text`: pode ser um bloco de thinking.
- `max_tokens` apertado num modelo que raciocina: a resposta vem cortada ou vazia.
- Confiar em `temperature=0` para ter determinismo; para saídas estáveis, use *structured outputs*.
- Comparar tokens entre modelos ou provedores (tokenizers diferentes).
- Vazar a API key no GitHub.

### Perguntas de fixação
1. Se a API é stateless, como o Claude Code "lembra" do que você fez 20 minutos atrás? O que acontece com o custo de cada turno à medida que a sessão cresce?
2. Por que o idioma dos prompts importa num sistema com 7 agentes trocando mensagens o tempo todo?
3. Como garantir que o Agente Revisor responda só "aprovar", "pedir mudanças" ou "escalar", sem usar temperature? (ponte para a Aula 0.2)

---

## 11. Glossário
| Termo | Significado |
|---|---|
| **Token** | Unidade de texto processada pelo modelo; base de cobrança e de limite |
| **Janela de contexto** | Tudo o que o modelo enxerga numa chamada (entrada + saída) |
| **Stateless** | A API não guarda nada entre chamadas; o histórico é reenviado pelo cliente |
| **Sampling / temperature** | Sorteio do próximo token; a temperature controlava o quanto a distribuição era aleatória |
| **Effort** | Parâmetro que controla quanto o modelo raciocina (substitui os budgets de thinking) |
| **Thinking adaptativo** | O modelo decide quanto raciocinar; os tokens de raciocínio contam como saída |
| **`stop_reason`** | Motivo de parada: `end_turn`, `max_tokens`, `tool_use`... |
| **Tool use / function calling** | O modelo **pede** uma ferramenta (nome + args JSON); **o código executa** |
| **Harness** | O programa em volta do modelo que executa ferramentas e gerencia o loop (por exemplo, o Claude Code) |
| **Structured outputs** | Saída garantida num schema (JSON, enum) |
| **MCP** | Model Context Protocol: padrão para expor ferramentas e dados a agentes |
| **A2A** | Agent-to-Agent: protocolo de comunicação entre agentes |
| **HITL** | Human-in-the-loop: humano como ponto de aprovação ou decisão |
| **Context engineering** | Decidir o que entra no contexto de cada chamada ou agente |
| **LLM-as-judge** | Usar um LLM para avaliar a saída de outro |

---

## 12. Fontes consultadas
| Fonte | Data | Tipo |
|---|---|---|
| [Models overview, Claude Platform Docs](https://platform.claude.com/docs/models/overview) | consultado em 09/11/2026 | primária |
| [Claude Haiku 5.5 migration guide](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) | atual (nov/2026) | primária |
| [Claude Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) | atual (nov/2026) | primária |
| [Token counting, Claude Platform Docs](https://platform.claude.com/docs/build-with-claude/token-counting) | atual (nov/2026) | primária |
| [GitHub Docs: Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) | atual | primária |
| [Apidog: Gemini API Free Tier 2026](https://apidog.com/blog/gemini-api-free-tier/) | out/2026 | secundária |
| [Imisofts: Gemini API Free Tier Limits](https://imisofts.com/blog/gemini-api-free-tier-limits/) | 21/10/2026 | secundária |
| [BYOK List: Free AI API keys 2026](https://byoklist.com/guides/free-ai-api-keys) | out/2026 | secundária |
| [InferenceHub: Free AI credits that reset](https://inferencehub.org/blog/free-ai-credits-that-reset-2026) | 2026 | secundária |
| [LiteLLM issue #13781: temperature no GPT-5](https://github.com/BerriAI/litellm/issues/13781) | ago/2025 ⚠️ >6 meses | secundária |

---

## 13. Anexo: instruções para o Claude Code

> Copie o bloco abaixo e envie ao Claude Code junto com este arquivo.
>
> **Nota (v1.1):** este anexo foi executado em 10/11/2026, por decisão da estudante na branch `claude/branch-folders-5r3hec` (e não em `docs/estrutura-do-estudo`). O bloco fica como registro.

```text
Contexto: este é o repositório de estudo EikiGabriel/orquestracao-agentes. Anexei o
GUIA_DE_ESTUDO.md, que é a fonte da verdade sobre o plano de estudo.

Tarefa: abra UM Pull Request que estruture o repositório a partir do guia.

1. Base: se o PR #1 (branch lab-00/setup-inicial) ainda não estiver mergeado,
   crie a branch a partir dele; se já estiver, a partir de main. NÃO altere o
   conteúdo de labs/lab00_fundamentos/ nem do .devcontainer.
2. Branch: docs/estrutura-do-estudo
3. Estrutura alvo:
   docs/
     GUIA_DE_ESTUDO.md        (o arquivo anexado, sem alterar o conteúdo)
     sistema-alvo.md          (seções 2 e 3 do guia)
     cronograma.md            (seção 5)
     decisoes.md              (tabela 4.2, em formato de log de decisões)
     glossario.md             (seção 11)
   modulos/
     modulo-00-fundamentos/README.md   (objetivo + aulas 0.1–0.3)
     modulo-00-fundamentos/aula-0.1-tokens-contexto.md (seção 10 completa)
     modulo-01-... até modulo-10-.../README.md (objetivo + tópicos da seção 6;
       marque "Status: não iniciado")
   labs/
     lab00_fundamentos/       (já existe; não mexer)
     lab01_... até lab08_.../README.md (objetivo + critério de pronto da seção 7,
       marcados como "preliminar")
   diario/
     README.md                (explica o diário: uma entrada por sessão)
     2026-11-09-sessao-01.md e 2026-11-10-sessao-02.md (resuma a partir do guia)
   .github/pull_request_template.md
     (seções: O que este PR faz · Como revisar · Critério de pronto [checklist]
      · Limitações conhecidas)
4. Atualize o README.md da raiz: um resumo curto + links para docs/, modulos/,
   labs/ e diario/, e a tabela de progresso dos labs.
5. Regras:
   - NÃO invente conteúdo de aulas futuras: só o que está no guia.
   - NÃO inclua chaves, .env nem dados pessoais.
   - Nomes de pastas em minúsculas, sem acento, com hífen.
   - Mantenha os links internos funcionando (links relativos).
6. Na descrição do PR, liste os arquivos criados, como revisar e o que ficou de fora.
```
