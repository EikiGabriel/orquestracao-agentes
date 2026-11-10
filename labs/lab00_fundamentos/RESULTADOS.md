# Resultados: Lab 0.1

## Execução base
- [x] Rodou no Claude Haiku 5.5
- Custo total estimado do lab (Claude): US$ ____

## A. Idioma
| Modelo | Tokens PT | Tokens EN | Razão PT/EN |
|---|---|---|---|
| Claude (Haiku 5.5) | 267 | 235 | 1,14 |

Texto: Dante, *Inferno*, Canto I (a loba), numa tradução portuguesa antiga (108 palavras), e uma tradução fiel em inglês, verso a verso (128 palavras). Contagem com `count_tokens`, sem custo.

| | PT | EN |
|---|---|---|
| Tokens | 267 | 235 |
| Palavras | 108 | 128 |
| Tokens por palavra | 2,47 | 1,84 |

A estrutura da mensagem soma cerca de 9 tokens fixos; tirando essa sobra, a razão continua 1,14.

Observação (por que o mesmo texto gasta quantidades diferentes de tokens em PT e EN?):
- **O vocabulário de tokens favorece o inglês.** O tokenizer é montado a partir dos pedaços de texto mais frequentes no material de treino, que é majoritariamente em inglês. Palavras comuns em inglês costumam virar 1 token inteiro; em português, a mesma ideia é quebrada em mais pedaços.
- **A diferença por palavra é maior que a total.** Por palavra, o português gasta 34% mais (2,47 contra 1,84). No total, só 14% mais, porque o português disse a mesma coisa com 20 palavras a menos: ele dispensa pronomes e auxiliares (*"she"*, *"it was"*) e flexiona o verbo dentro da própria palavra (*investe*, *receia*). Cada palavra carrega mais informação e, por isso, mais tokens.
- **Acentos e palavras raras pesam.** Palavras arcaicas como *conspeto*, *torvação*, *enleia* e *excrucia* quase não aparecem nos textos de treino, então são quebradas em vários pedaços. Letras acentuadas (*ã*, *ç*, *é*) também tendem a gerar pedaços extras.
- **O número vale para este texto e este modelo.** Por ser poético e arcaico, este trecho provavelmente exagera a diferença; um texto comum do dia a dia deve dar uma razão mais perto de 1. E outros modelos ou provedores usam outros tokenizers, então a contagem não se compara entre eles.
- **Consequência prática:** num sistema com 7 agentes trocando mensagens o tempo todo, escrever os prompts em português custa mais tokens (e dinheiro, e espaço na janela de contexto) do que em inglês. É a resposta para a pergunta de fixação 2.

## B. Stateless
Em uma frase, com as suas palavras: por que a chamada 2 falhou sem o histórico?

>

## C. Corte
- Motivo de parada com `max_tokens=50`:
- Veio texto? Se não, por quê?

## Bônus
Mensagem de erro do `temperature=0`:

```
```

## Perguntas de fixação (Aula 0.1)
1. Se a API é stateless, como o Claude Code "lembra" do que você fez 20 minutos atrás? O que acontece com o custo de cada turno à medida que a sessão cresce?

>

2. Por que o idioma dos prompts importa num sistema com 7 agentes trocando mensagens?

>

3. Como garantir que o Agente Revisor responda só "aprovar", "pedir mudanças" ou "escalar", sem usar temperature?

>
