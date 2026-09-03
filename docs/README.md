# Documentação do MVP

> Documentação para avaliadores. Cada tópico tem um **`.md` principal** (leitura direta) e, quando necessário, `.md`s secundários com detalhes (mantendo os detalhes acessíveis sem poluir a leitura principal).

## Índice de tópicos

| Tópico (enunciado item 5) | Principal | Detalhes |
|---|---|---|
| Contexto de Negócios e Perguntas (Etapas 2 e 4.1) | [contexto-e-perguntas/README.md](contexto-e-perguntas/README.md) | [perguntas](contexto-e-perguntas/perguntas.md) · [definições operacionais](contexto-e-perguntas/definicoes.md) |
| Carga dos Dados (Etapa 4.2) | [carga-dos-dados/README.md](carga-dos-dados/README.md) | [origem dos dados](carga-dos-dados/fontes.md) |
| Modelagem e Catálogo de Dados (Etapa 4.3) | [modelagem-e-catalogo/README.md](modelagem-e-catalogo/README.md) | [catálogo CNO](modelagem-e-catalogo/catalogo-cno.md) · [DTB](modelagem-e-catalogo/catalogo-dtb.md) · [população](modelagem-e-catalogo/catalogo-populacao.md) · [dim_data](modelagem-e-catalogo/catalogo-dim-data.md) |
| Pipeline de Dados (Etapa 4.4) | [pipeline-de-dados/README.md](pipeline-de-dados/README.md) | [helpers](pipeline-de-dados/helpers.md) |
| Qualidade de Dados (Etapa 4.5) | — pendente — | |
| Análise de Dados (Etapa 4.5) | — pendente — | |
| Autoavaliação | — pendente — | |

## ⚠️ Sincronização: docs ↔ código ↔ catálogo

Os arquivos de documentação **duplicam conteúdo que também existe no código** (comentários de coluna, regras de transformação, definições de escopo). Essa duplicação é intencional (o avaliador lê os `docs/`; o Databricks executa o código), mas **exige sincronia**.

**Sempre que o código ou o catálogo mudar, atualizar os docs correspondentes na mesma entrega:**

| Fonte da verdade (código) | Espelho na documentação |
|---|---|
| `ETL/catalogo/*.py` (dicionários de comentários/domínios) | `docs/modelagem-e-catalogo/catalogo-*.md` |
| Regras/transformações dos notebooks | markdown do próprio notebook **e** `docs/contexto-e-perguntas/definicoes.md` (decisões de escopo) |
| Decisões de análise (ex.: qualidade) | `docs/contexto-e-perguntas/definicoes.md` e tópico Qualidade/Análise |
| Novas tabelas/colunas | catálogo + `docs/modelagem-e-catalogo/*` + diagrama do `README.md` |

**Checklist ao alterar algo:**
- [ ] Atualizar `ETL/catalogo/*.py` (comentários de coluna/domínios) e reaplicar `add_column_comments` no Databricks.
- [ ] Atualizar o espelho em `docs/modelagem-e-catalogo/catalogo-*.md`.
- [ ] Atualizar o markdown do notebook afetado (células de descrição de transformações).
- [ ] Atualizar decisões de escopo/limitações em `docs/contexto-e-perguntas/definicoes.md` quando houver impacto nas perguntas.