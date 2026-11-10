# Lab 2: Pipeline Dev → Revisor

> **Preliminar.** O roteiro e o critério de pronto serão detalhados quando a aula correspondente for dada.

**Status:** não iniciado · **Módulo:** [modulo-02-padroes-de-orquestracao](../../modulos/modulo-02-padroes-de-orquestracao/README.md)

O Agente Desenvolvedor gera código a partir de uma spec; o Revisor devolve uma **saída estruturada** (`veredito` ∈ {aprovar, pedir_mudancas, escalar} + lista de problemas); até N rodadas.
**Pronto quando:** o pipeline converge ou escala; registra rodadas, tokens e custo por execução; o `llm.py` (wrapper entre provedores) está criado.

---
Fonte: [GUIA_DE_ESTUDO.md, seção 7](../../docs/GUIA_DE_ESTUDO.md#7-laboratórios) (v1.1).
