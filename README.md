# MVP — Engenharia de Dados

**Tema:** Panorama do tamanho das casas populares e unifamiliares conforme o Cadastro Nacional de Obras (CNO).

Pipeline de dados ponta a ponta (coleta → modelagem → carga → análise) em **Databricks** (arquitetura medalhão bronze/silver/gold, Delta Lake, catálogo de dados). Dados: CNO (dados.gov.br/RFB), DTB (IBGE) e estimativas populacionais (IBGE via Base dos Dados).

---

## Documentação por tópico

> Cada tópico tem um `.md` principal (leitura direta) e `.md`s secundários com detalhes. A organização completa está em [`docs/README.md`](docs/README.md).

| # | Tópico | Documento |
|---|---|---|
| 1 | **Contexto de Negócios e Perguntas** (Etapas 2 e 4.1) | [docs/contexto-e-perguntas](docs/contexto-e-perguntas/README.md) |
| 2 | **Carga dos Dados** (Etapa 4.2) | [docs/carga-dos-dados](docs/carga-dos-dados/README.md) |
| 3 | **Modelagem e Catálogo de Dados** (Etapa 4.3) | [docs/modelagem-e-catalogo](docs/modelagem-e-catalogo/README.md) |
| 4 | **Pipeline de Dados** (Etapa 4.4) | [docs/pipeline-de-dados](docs/pipeline-de-dados/README.md) |
| 5 | **Qualidade de Dados** (Etapa 4.5) | [docs/qualidade-de-dados](docs/qualidade-de-dados/README.md) |
| 6 | **Análise de Dados** (Etapa 4.5) | [docs/analise-de-dados](docs/analise-de-dados/README.md) |
| 7 | **Autoavaliação** | [docs/autoavaliacao](docs/autoavaliacao/README.md) |

## Evidências

Screenshots de execução e resultados: [`docs/evidencias/`](docs/evidencias/).

## Repositório — estrutura

```
src/data_pipeline/            # helpers reutilizáveis (read/write, qualidade, geografia)
ETL/
  catalogo/                   # catálogo de dados (comentários de colunas e domínios)
  notebooks/                  # pipeline por domínio (bronze → silver → gold)
qualidade/                    # análise de qualidade de dados
analise/                      # respostas às perguntas do objetivo
docs/                         # documentação para o avaliador (este arquivo + tópicos)
```