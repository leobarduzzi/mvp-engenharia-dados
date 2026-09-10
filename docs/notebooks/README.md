# Notebooks executados (HTML)

> HTMLs exportados dos **notebooks executados no Databricks** (File → **Export → HTML**), com as saídas dos scripts. Servidos via **GitHub Pages**.
> Os arquivos `.html` ficam nesta pasta (`docs/notebooks/`); o notebook `.ipynb` original fica no repositório.

## Como gerar / atualizar

1. Abra o notebook no Databricks (já executado);
2. **File → Export → HTML**;
3. Salve nesta pasta com o **nome exato** da coluna *Arquivo HTML* da tabela abaixo;
4. Commit + push — o GitHub Pages publica automaticamente.

> Prefixos usados para evitar colisão de nomes: `qualidade_` e `analise_` (há dois notebooks chamados `cadastro_nacional_obras`).

## Índice

### Pipeline (ETL)

| Notebook | Arquivo HTML | Código (.ipynb) |
|---|---|---|
| `01_bronze_cno` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_cno.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/01_bronze_cno.ipynb) |
| `01_bronze_cno_areas` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_cno_areas.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/01_bronze_cno_areas.ipynb) |
| `02_silver_cno` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_cno.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/02_silver_cno.ipynb) |
| `02_silver_cno_areas` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_cno_areas.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/02_silver_cno_areas.ipynb) |
| `03_gold_dim_area` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_dim_area.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/03_gold_dim_area.ipynb) |
| `03_gold_dim_situacao` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_dim_situacao.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/03_gold_dim_situacao.ipynb) |
| `04_gold_fato_obras` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/04_gold_fato_obras.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/cadastro_nacional_obras/04_gold_fato_obras.ipynb) |
| `01_gold_dim_data` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_gold_dim_data.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/dimensao_data/01_gold_dim_data.ipynb) |
| `01_bronze_dtb` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_dtb.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/divisao_territorial_brasileira/01_bronze_dtb.ipynb) |
| `02_silver_municipios` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_municipios.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/divisao_territorial_brasileira/02_silver_municipios.ipynb) |
| `03_gold_dim_municipio` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_dim_municipio.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/divisao_territorial_brasileira/03_gold_dim_municipio.ipynb) |
| `01_bronze_populacao` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/01_bronze_populacao.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/populacao/01_bronze_populacao.ipynb) |
| `02_silver_populacao` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/02_silver_populacao.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/populacao/02_silver_populacao.ipynb) |
| `03_gold_fato_populacao` | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/03_gold_fato_populacao.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/ETL/notebooks/populacao/03_gold_fato_populacao.ipynb) |

### Qualidade de Dados

| Notebook | Arquivo HTML | Código (.ipynb) |
|---|---|---|
| `cadastro_nacional_obras` (qualidade) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/qualidade_cadastro_nacional_obras.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/qualidade/cadastro_nacional_obras.ipynb) |

### Análise de Dados

| Notebook | Arquivo HTML | Código (.ipynb) |
|---|---|---|
| `cadastro_nacional_obras` (análise) | [html](https://leobarduzzi.github.io/mvp-engenharia-dados/notebooks/analise_cadastro_nacional_obras.html) | [ipynb](https://github.com/leobarduzzi/mvp-engenharia-dados/blob/main/analise/cadastro_nacional_obras.ipynb) |