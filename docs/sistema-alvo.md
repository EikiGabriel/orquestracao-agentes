# Sistema-alvo

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

## Humano no loop (HITL)
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
Fonte: [GUIA_DE_ESTUDO.md, seções 2 e 3](GUIA_DE_ESTUDO.md#2-o-sistema-alvo) (v1.1).
