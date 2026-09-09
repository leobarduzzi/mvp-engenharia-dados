# Perguntas de negócio

> [← Voltar para o README do tópico](README.md)

> Lista viva de perguntas do objetivo. **Nunca remover perguntas não respondidas** — o que não for atingido é discutido na Autoavaliação.
> Status possíveis: `em aberto`, `respondida`, `não respondida`.

---

## P1 — Houve variação no tempo da área média das casas (unifamiliares e populares)?

- **O que pergunta:** como a metragem média das casas evoluiu ao longo do tempo (por ano/década de início da obra).
- **Por que importa:** sinaliza tendências de adensamento, custo de terreno e efeito de políticas habitacionais sobre o tamanho das residências.
- **Como responder (dados):** agregar `fato_obras` filtrado às destinações **Residencial unifamiliar** e **Casa popular**; agrupar por ano de início via `dim_data.ano` (`sk_data_inicio`); calcular a média de `metragem` (ver [Definições operacionais](definicoes.md)); analisar a série temporal e a estabilidade da amostra por ano.
- **Resultado:** análise executada no [notebook de análise](../../analise/cadastro_nacional_obras.ipynb) — mudança de cobertura do cadastro em 2019 + sub-representação de casas ≤ 70 m² impedem conclusão. Detalhes: [Análise de Dados](../analise-de-dados/README.md).
- **Status:** `não respondida` (não conclusiva).

## P2 — O tamanho populacional do município se relaciona com a área construída? E o tamanho populacional da região geográfica imediata?

- **O que pergunta:** se municípios (e regiões geográficas imediatas) mais populosos apresentam casas menores ou maiores — ou seja, se adensamento/pressão urbana se refletem na área construída.
- **Por que importa:** ajuda a entender a relação entre ocupação populacional e porte das residências, útil para planejamento urbano e habitacional.
- **Como responder (dados):** join `fato_obras` → `dim_municipio` (UF, região geográfica imediata) → `fato_populacao` (município × ano); comparar a metragem média das casas por faixa de população do município e da região imediata; verificar correlação.
- **Resultado:** associação positiva nas regiões imediatas mais populosas, **sem evidência de causalidade** (análise agregada). Detalhes: [Análise de Dados](../analise-de-dados/README.md).
- **Status:** `respondida` (com ressalvas).

## P3 — Qual a distribuição das situações (ativa, paralisada, encerrada etc.) por porte de obra? Obras menores têm mais chance de ficarem paralisadas/nulas?

- **O que pergunta:** se o porte da obra (metragem da área principal) se associa ao estado cadastral no CNO — em especial, se obras menores ficam mais sujeitas a `PARALISADA`/`NULA`.
- **Por que importa:** conecta o tamanho das casas ao ciclo de vida da obra; obras paralisadas/nulas podem indicar informalidade ou inviabilidade econômica de empreendimentos pequenos.
- **Como responder (dados):** cruzar `fato_obras` (via `sk_situacao`) com `dim_situacao`; comparar a distribuição da metragem (área principal) por situação e a taxa de paralisação/nula por faixa de metragem.
- **Resultado:** a proporção de `PARALISADA`/`NULA` **aumenta com a metragem** — hipótese de maior risco em obras menores não confirmada (na base registrada). Detalhes: [Análise de Dados](../analise-de-dados/README.md).
- **Status:** `respondida`.

