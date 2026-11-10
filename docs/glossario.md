# Glossário

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
Fonte: [GUIA_DE_ESTUDO.md, seção 11](GUIA_DE_ESTUDO.md#11-glossário) (v1.1).
