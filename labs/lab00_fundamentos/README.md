# Lab 0.1: Tokens, janela de contexto e a API sem memória

**Aula:** Módulo 0, Aula 0.1
**Tempo estimado:** 1h
**Arquivo base:** [`primeira_chamada.py`](primeira_chamada.py)

## Preparação
1. Abra este repositório no Codespaces: **Code → Codespaces → Create codespace on main**. As dependências são instaladas sozinhas.
2. Cadastre `ANTHROPIC_API_KEY` e `ANTHROPIC_MODEL` como Codespaces secrets em github.com/settings/codespaces, ou copie `.env.example` para `.env` e preencha. Nas sessões do Claude Code na nuvem, use o nome `LAB_ANTHROPIC_API_KEY` para a chave.
3. Rode:
   ```bash
   python labs/lab00_fundamentos/primeira_chamada.py
   ```
   Aparecem a resposta, o motivo de parada, os tokens e o custo estimado.

## Experimentos
Escreva o código de cada experimento você mesma, num arquivo novo nesta pasta (por exemplo, `experimentos.py`), reaproveitando as funções do arquivo base.

- **A. Idioma.** Pegue um parágrafo de cerca de 100 palavras em PT e a tradução em EN. Conte os tokens dos dois no Claude e calcule a razão PT/EN.
- **B. Stateless.** Chamada 1: "Meu número favorito é 42." Chamada 2, sem enviar o histórico: "Qual é meu número favorito?" Depois repita a chamada 2 enviando o histórico completo (user → assistant → user).
- **C. Corte.** Peça uma explicação longa com `max_tokens=50` (no Claude) e observe o motivo de parada e se veio algum texto.
- **Bônus.** Passe `temperature=0` para o Claude e leia a mensagem de erro.

## Critério de pronto
Preencha [`RESULTADOS.md`](RESULTADOS.md) e abra um PR. Eu reviso.
