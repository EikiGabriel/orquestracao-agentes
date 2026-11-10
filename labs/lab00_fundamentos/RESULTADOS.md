# Resultados: Lab 0.1

## Execução base
- [x] Rodou no Claude Haiku 5.5
- Custo total estimado do lab (Claude): US$ 0,0003 até agora (execução base US$ 0,000062 + B e C US$ 0,000244; o A usa `count_tokens` e não custa nada). Falta o bônus, que dá erro e não deve custar nada.

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

> Porque a API não guarda nada entre chamadas: a chamada 2 chegou só com a pergunta, e o "42" estava na chamada 1, que o modelo nunca mais viu.

| Chamada | O que foi enviado | Resposta | Tokens in / out |
|---|---|---|---|
| 1 | "Meu número favorito é 42." | Comentou o 42 do *Guia do Mochileiro das Galáxias* | 19 / 201 |
| 2, sem histórico | só "Qual é meu número favorito?" | "Não sei! Não tenho acesso a informações sobre você além do que você me conta nesta conversa…" | 19 / 163 |
| 2, com histórico | user → assistant → user | "Pelo que você me disse, seu número favorito é o 42." | 166 / 23 |

Observações:
- **A memória é o histórico que eu reenvio.** Com o histórico, o modelo "lembrou" porque o fato estava de novo na mesa, não porque guardou algo.
- **Lembrar custa caro.** A entrada saltou de 19 para 166 tokens (quase 9x), porque reenviei a chamada 1 inteira, incluindo a resposta longa do modelo. Numa conversa longa, cada turno reenvia tudo o que veio antes e fica mais caro que o anterior.
- **O raciocínio também é cobrado.** Nas chamadas 1 e 2 sem histórico, a resposta veio com um bloco `thinking` antes do `text`: as respostas eram curtas, mas a saída foi de 201 e 163 tokens. Com o histórico, a pergunta ficou fácil e o modelo respondeu direto (só `text`, 23 tokens).

## C. Corte
- Motivo de parada com `max_tokens=50`: `max_tokens`
- Veio texto? Se não, por quê? **Não.** A resposta só teve um bloco `thinking` (`blocos: ['thinking']`, out=50). O modelo raciocina antes de escrever, e o raciocínio conta no `max_tokens`: os 50 tokens acabaram ainda no raciocínio, antes de começar o texto. Por isso um teto baixo num modelo que raciocina pode devolver uma resposta vazia, e é preciso olhar o `stop_reason` em vez de supor que veio texto.

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
