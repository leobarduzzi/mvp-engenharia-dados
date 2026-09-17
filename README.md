# MVP — Engenharia de Dados

**Tema:** Panorama do tamanho das casas populares e unifamiliares conforme o Cadastro Nacional de Obras (CNO).

Pipeline de dados ponta a ponta (coleta → modelagem → carga → análise) em **Databricks** (arquitetura medalhão bronze/silver/gold, Delta Lake, catálogo de dados). Dados: CNO (dados.gov.br/RFB), DTB (IBGE) e estimativas populacionais (IBGE via Base dos Dados).

---

## Documentação por tópico

> Cada tópico tem um `.md` principal (leitura direta) e `.md`s secundários com detalhes.

| # | Tópico | Documento |
|---|---|---|
| 1 | **Contexto de Negócios e Perguntas** | [docs/contexto-e-perguntas](docs/contexto-e-perguntas/README.md) |
| 2 | **Carga dos Dados** | [docs/carga-dos-dados](docs/carga-dos-dados/README.md) |
| 3 | **Modelagem e Catálogo de Dados** | [docs/modelagem-e-catalogo](docs/modelagem-e-catalogo/README.md) |
| 4 | **Pipeline de Dados** | [docs/pipeline-de-dados](docs/pipeline-de-dados/README.md) |
| 5 | **Qualidade de Dados** | [docs/qualidade-de-dados](docs/qualidade-de-dados/README.md) |
| 6 | **Análise de Dados** | [docs/analise-de-dados](docs/analise-de-dados/README.md) |
| 7 | **Autoavaliação** | [docs/autoavaliacao](docs/autoavaliacao/README.md) |

## Evidências

### Notebooks executados

Cada notebook possui o **código** (`.ipynb` no repositório) e a **execução com saídas** (`.html` via GitHub Pages).

#### Pipeline (ETL)

##### Bronze

| Notebook | Código (.ipynb) | Execução (.html) |
|---|---|---|
| `01_bronze_cno` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/01_bronze_cno.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_cno.html) |
| `01_bronze_cno_areas` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/01_bronze_cno_areas.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_cno_areas.html) |
| `01_bronze_dtb` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/divisao_territorial_brasileira/01_bronze_dtb.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_dtb.html) |
| `01_bronze_populacao` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/populacao/01_bronze_populacao.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_populacao.html) |

##### Silver

| Notebook | Código (.ipynb) | Execução (.html) |
|---|---|---|
| `02_silver_cno` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/02_silver_cno.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_cno.html) |
| `02_silver_cno_areas` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/02_silver_cno_areas.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_cno_areas.html) |
| `02_silver_municipios` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/divisao_territorial_brasileira/02_silver_municipios.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_municipios.html) |
| `02_silver_populacao` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/populacao/02_silver_populacao.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_populacao.html) |

##### Gold

| Notebook | Código (.ipynb) | Execução (.html) |
|---|---|---|
| `03_gold_dim_area` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/03_gold_dim_area.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_dim_area.html) |
| `03_gold_dim_situacao` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/03_gold_dim_situacao.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_dim_situacao.html) |
| `04_gold_fato_obras` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/04_gold_fato_obras.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/04_gold_fato_obras.html) |
| `01_gold_dim_data` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/dimensao_data/01_gold_dim_data.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_gold_dim_data.html) |
| `03_gold_dim_municipio` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/divisao_territorial_brasileira/03_gold_dim_municipio.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_dim_municipio.html) |
| `03_gold_fato_populacao` | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/populacao/03_gold_fato_populacao.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_fato_populacao.html) |

#### Qualidade de Dados

| Notebook | Código (.ipynb) | Execução (.html) |
|---|---|---|
| `cadastro_nacional_obras` (qualidade) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/qualidade/cadastro_nacional_obras.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/qualidade_cadastro_nacional_obras.html) |

#### Análise de Dados

| Notebook | Código (.ipynb) | Execução (.html) |
|---|---|---|
| `cadastro_nacional_obras` (análise) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/analise/cadastro_nacional_obras.ipynb) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/analise_cadastro_nacional_obras.html) |

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