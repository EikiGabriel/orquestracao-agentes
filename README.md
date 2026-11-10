# orquestracao-agentes

Estudo prático de **orquestração de agentes de IA**, dos fundamentos de LLMs até um sistema multiagente para desenvolvimento de software com humano no loop.

## O sistema-alvo
Um **orquestrador** distribui o trabalho entre agentes especializados: Desenvolvedor, Revisor, Guardrails, Boas Práticas, Otimização, Contexto/Memória e Assistente Administrativo. O humano é acionado para aprovar PRs, em casos de baixa confiança, requisitos ambíguos e ações irreversíveis.

## Estrutura
```
labs/
  lab00_fundamentos/   # Módulo 0: tokens, contexto, primeira chamada
.devcontainer/         # ambiente pronto para o GitHub Codespaces
.env.example           # chaves e modelos (copie para .env, que NUNCA vai para o git)
requirements.txt       # SDKs oficiais: anthropic, openai, google-genai
```

## Como rodar
1. **Code → Codespaces → Create codespace on main**
2. Cadastre `ANTHROPIC_API_KEY`, `GEMINI_API_KEY` e `OPENAI_API_KEY` como Codespaces secrets, ou crie um `.env` a partir do `.env.example`.
3. Siga o README de cada lab.

## Regras do repositório
- **Nenhuma chave de API no código ou nos commits.** O `.env` está no `.gitignore`.
- Nada de código ou dados de empresa: os tiers gratuitos usam os dados enviados para treinar modelos.
- Cada lab entra por Pull Request, revisado antes do merge.

## Progresso
| Lab | Tema | Status |
|---|---|---|
| 0.1 | Tokens, contexto, API stateless | em andamento |
| 1 | Agente com 1 ferramenta | — |
| 2 | Pipeline Dev → Revisor | — |
| 3 | Orquestrador com roteamento | — |
| 4 | Agente de Contexto | — |
| 5 | Guardrails + prompt injection | — |
| 6 | HITL: PR e pausa para aprovação | — |
| 7 | Evals e tracing | — |
| 8 | Otimização de custo/latência | — |
