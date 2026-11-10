# Log de decisões

Uma entrada por decisão, em ordem cronológica. Decisões novas entram no fim, com o próximo número, e também na tabela 4.2 do guia.

### D01 · 09/11/2026
- **Decisão:** Labs em **Python**
- **Motivo:** Linguagem dominada

### D02 · 09/11/2026
- **Decisão:** **Claude Haiku 5.5** (`claude-haiku-5-5`) como modelo pago padrão
- **Motivo:** O mais barato da linha atual da Anthropic

### D03 · 09/11/2026
- **Decisão:** Ler a resposta da API **pelo `type` dos blocos**, nunca por posição
- **Motivo:** A resposta pode começar com blocos `thinking`

### D04 · 09/11/2026
- **Decisão:** **Não usar `temperature`/`top_p`/`top_k`** nos modelos Claude 5.5
- **Motivo:** Retornam erro 400; o comportamento se guia pelo prompt e pelo `effort`

### D05 · 09/11/2026
- **Decisão:** Orçamento de **US$10/mês** em API paga, usando antes os tiers gratuitos
- **Motivo:** Custo de estudo controlado

### D06 · 09/11/2026
- **Decisão:** Wrapper próprio e fino entre provedores (`llm.py`) a partir do Lab 2; **nenhum framework antes do Módulo 5**
- **Motivo:** Entender o mecanismo antes da abstração. *A reavaliar (10/11/2026): com um só provedor, o wrapper pode não ser necessário.*

### D07 · 10/11/2026
- **Decisão:** Repositório **privado** `EikiGabriel/orquestracao-agentes`; tudo entra por **PR**
- **Motivo:** Versionamento + prática de HITL

### D08 · 10/11/2026
- **Decisão:** Execução no **GitHub Codespaces** com devcontainer; chaves como *Codespaces secrets*
- **Motivo:** Contorna as restrições do computador da empresa

### D09 · 10/11/2026
- **Decisão:** Usar **só o Claude Haiku 5.5**; Gemini e OpenAI saem do estudo (PR #2)
- **Motivo:** Simplificar: um provedor, um SDK, uma chave

### D10 · 10/11/2026
- **Decisão:** **Não versionar o `.env`**; o `.env.example` continua como modelo sem segredos
- **Motivo:** Uma chave commitada fica no histórico do git para sempre

### D11 · 10/11/2026
- **Decisão:** Nas sessões do **Claude Code na nuvem**, a chave fica em `LAB_ANTHROPIC_API_KEY` (PR #3, issue #4)
- **Motivo:** Lá a variável `ANTHROPIC_API_KEY` não chega ao script; o código lê `LAB_ANTHROPIC_API_KEY` e, se não existir, `ANTHROPIC_API_KEY`

---
Fonte: [GUIA_DE_ESTUDO.md, seção 4.2](GUIA_DE_ESTUDO.md#42-registro-de-decisões) (v1.1).
