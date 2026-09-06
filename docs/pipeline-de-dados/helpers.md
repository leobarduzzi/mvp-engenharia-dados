# Helpers reutilizáveis (`src/data_pipeline`)

> Detalhamento do pacote de código reutilizável do projeto, usado por todos os notebooks do pipeline.

## Princípio

> **Métodos reutilizáveis ficam em `src/data_pipeline`; os notebooks apenas orquestram o fluxo.** Nenhuma lógica de leitura, escrita, normalização ou metadados é duplicada nos notebooks.

Benefícios: **DRY** (uma implementação única para todos os domínios), **robustez** (encapsula decisões difíceis, ex.: cast tolerante no modo ANSI do Databricks), **consistência** (nomes de colunas sempre via `normalizar_colunas`) e **manutenção** (correção feita uma vez no helper).

## `data_utils.py`

| Função | O que faz | Uso |
|---|---|---|
| `read_csv(spark, file_path, delimiter, encoding, header, infer_schema)` | Lê CSV com encoding configurável (padrão `Windows-1252`) | Ingestão bronze (`01_bronze_cno`, `01_bronze_cno_areas`, `01_bronze_populacao`) |
| `read_ods(spark, file_path, sheet_name, header)` | Lê `.ods` convertendo células para texto limpo (preserva códigos como `1100015`, sem `.0`) | Ingestão bronze DTB (`01_bronze_dtb`) |
| `save_table(df, table_name, mode)` | Persiste DataFrame como tabela **Delta** (`saveAsTable`) | Persistência de todas as camadas (bronze/silver/gold) |
| `normalizar_colunas(df)` | Normaliza nomes de colunas (minúsculas, sem acento, `_`) e **falha** se gerar duplicados | Ingestão de todos os domínios |
| `normalizar_texto(nome)` | Normaliza um texto para o padrão do projeto | Base de `normalizar_colunas` |
| `para_double_seguro(coluna)` | Converte para `double` de forma tolerante (aceita vírgula decimal; inválido → `null`) | `area_total`, `metragem` na silver |
| `para_data_segura(coluna, formato)` | Converte para `date` de forma tolerante (valida `yyyy-MM-dd`; inválido → `null`) | `data_de_inicio`, `data_da_situacao` na silver |
| `nulo_se_vazio(coluna)` | `''`/`'null'` (qualquer caixa) viram `null` de verdade | Limpeza de campos textuais gov.br |
| `mapear_valores(coluna, mapa)` | Substitui valores via dicionário `{de: para}` (when encadeado) | Decodificação de códigos em dimensões |
| `add_column_comments(spark, table_name, comments)` | Aplica `COMMENT` em cada coluna (`ALTER TABLE ... ALTER COLUMN`) | Aplicação do catálogo logo após `save_table` |
| `add_table_comment(spark, table_name, comment)` | Aplica o `COMMENT` da tabela (`ALTER TABLE ... SET TBLPROPERTIES`) | Comentário descritivo da tabela logo após `save_table` |

## `quality.py`

| Função | O que faz | Uso |
|---|---|---|
| `resumo_invalidos(spark, df, regras)` | Para cada regra (`True = inválido`), retorna `qtd_invalidos` e `pct_sobre_total` | Relatório de qualidade na silver (CNO, áreas, municípios, população) |
| `condicao_valida(regras)` | Combina as regras em uma expressão `True = registro válido` | Filtro de qualidade antes de persistir |

## `tom_utils.py`

| Função | O que faz | Uso |
|---|---|---|
| `enriquecer_codigo_tom(spark, df, coluna_codigo_ibge, coluna_codigo_tom)` | Adiciona o **código TOM** (4 dígitos, SIAFI/Tesouro) a partir do código IBGE via `cidade-ibge-tom` (MIT); join `left` no driver | `02_silver_municipios` — habilita o join do CNO com a dimensão de municípios |

## `regioes.py`

| Função | O que faz | Uso |
|---|---|---|
| `adicionar_regiao(df, coluna_sigla_uf)` | Adiciona a coluna `regiao` (Norte, Nordeste, Centro-Oeste, Sudeste, Sul) a partir da sigla da UF (mapa oficial IBGE); UFs sem mapeamento ficam `null` | Análise (P1 por região) — notebook `analise/cadastro_nacional_obras.ipynb` |

---

## Exemplo de uso no pipeline

No `02_silver_cno`: `read_csv` (bronze) → `para_data_segura`/`para_double_seguro` (tipos tolerantes) → `resumo_invalidos` (qualidade) → `condicao_valida` (filtro) → `save_table` (Delta) → `add_column_comments` (catálogo de colunas) → `add_table_comment` (comentário da tabela). Nenhuma dessas etapas é reimplementada no notebook.