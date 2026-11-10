# orquestracao-agentes

Estudo prático de **orquestração de agentes de IA**, dos fundamentos de LLMs até um sistema multiagente para desenvolvimento de software com humano no loop. Os labs usam Python e o **Claude Haiku 5.5**, sem frameworks até o Módulo 5.

A fonte da verdade do estudo é o [Guia de Estudo](docs/GUIA_DE_ESTUDO.md).

## O sistema-alvo
Um **orquestrador** distribui o trabalho entre agentes especializados: Desenvolvedor, Revisor, Guardrails, Boas Práticas, Otimização, Contexto/Memória e Assistente Administrativo. O humano é acionado para aprovar PRs, em casos de baixa confiança, requisitos ambíguos e ações irreversíveis. Detalhes em [docs/sistema-alvo.md](docs/sistema-alvo.md).

## Estrutura
| Pasta | Conteúdo |
|---|---|
| [`docs/`](docs/) | [Guia de estudo](docs/GUIA_DE_ESTUDO.md), [sistema-alvo](docs/sistema-alvo.md), [cronograma](docs/cronograma.md), [decisões](docs/decisoes.md) e [glossário](docs/glossario.md) |
| [`modulos/`](modulos/) | Um README por módulo (objetivo, tópicos, status) e as notas de cada aula |
| [`labs/`](labs/) | Um lab por pasta: roteiro (`README.md`), código e entrega (`RESULTADOS.md`) |
| [`diario/`](diario/) | Uma entrada por sessão de estudo |
| `.devcontainer/` | Ambiente pronto para o GitHub Codespaces |
| `.github/` | Template de Pull Request |
| `.env.example` | Chave e modelo (copie para `.env`, que **nunca** vai para o git) |
| `requirements.txt` | SDK oficial da Anthropic |

## Como rodar
1. **Code → Codespaces → Create codespace on main**
2. Cadastre `ANTHROPIC_API_KEY` e `ANTHROPIC_MODEL` como Codespaces secrets, ou crie um `.env` a partir do `.env.example`. Nas sessões do Claude Code na nuvem, cadastre a chave como `LAB_ANTHROPIC_API_KEY`.
3. Siga o README de cada lab.

## Regras do repositório
- **Nenhuma chave de API no código ou nos commits.** O `.env` está no `.gitignore`.
- Nada de código ou dados de empresa.
- Tudo entra por Pull Request, revisado antes do merge.

## Progresso
| Módulo | Lab | Tema | Status |
|---|---|---|---|
| [0](modulos/modulo-00-fundamentos/README.md) | [0.1](labs/lab00_fundamentos/README.md) | Tokens, contexto, API stateless | em andamento |
| [1](modulos/modulo-01-do-prompt-ao-agente/README.md) | [1](labs/lab01_agente_com_ferramenta/README.md) | Agente com 1 ferramenta | — |
| [2](modulos/modulo-02-padroes-de-orquestracao/README.md) | [2](labs/lab02_pipeline_dev_revisor/README.md) | Pipeline Dev → Revisor | — |
| [2](modulos/modulo-02-padroes-de-orquestracao/README.md) | [3](labs/lab03_orquestrador_roteamento/README.md) | Orquestrador com roteamento | — |
| [3](modulos/modulo-03-context-engineering-e-memoria/README.md) | [4](labs/lab04_agente_de_contexto/README.md) | Agente de Contexto | — |
| [4](modulos/modulo-04-protocolos/README.md) | — | Protocolos (MCP, A2A) | — |
| [5](modulos/modulo-05-frameworks-e-sdks/README.md) | — | Frameworks e SDKs (spike comparativo) | — |
| [6](modulos/modulo-06-guardrails-e-seguranca/README.md) | [5](labs/lab05_guardrails_injection/README.md) | Guardrails + prompt injection | — |
| [7](modulos/modulo-07-human-in-the-loop/README.md) | [6](labs/lab06_hitl_pr/README.md) | HITL: PR e pausa para aprovação | — |
| [8](modulos/modulo-08-avaliacao-e-observabilidade/README.md) | [7](labs/lab07_evals_tracing/README.md) | Evals e tracing | — |
| [9](modulos/modulo-09-otimizacao/README.md) | [8](labs/lab08_otimizacao/README.md) | Otimização de custo/latência | — |
| [10](modulos/modulo-10-projeto-final/README.md) | — | Projeto final: sistema completo | — |
