# Modelagem e Catálogo de Dados (Etapa 4.3)

> Documento principal do tópico **"Modelagem e Catálogo de Dados"**.
> Catálogo de dados transcrito por domínio:
> [CNO](catalogo-cno.md) · [DTB](catalogo-dtb.md) · [População](catalogo-populacao.md) · [Dimensão de data](catalogo-dim-data.md)

---

## Escolha do modelo: Star Schema

O modelo escolhido foi o **Esquema Estrela** (Star Schema), estrutura clássica de Data Warehouse otimizada para consultas analíticas.

**Justificativa:** as perguntas do objetivo analisam fatos (obras de construção civil e população) sob múltiplas dimensões (tempo, localização, situação, perfil da área). O esquema estrela:
- centraliza as medidas em **fatos** e as classificações em **dimensões** desnormalizadas — leitura simples e rápida;
- evita joins complexos em cascata (caso do Snowflake), o que importa no cluster limitado da versão gratuita;
- permite reuso de dimensões conformadas (`dim_data`, `dim_municipio`) entre fatos.

## Diagrama do modelo
![DER do modelo Gold](..\evidencias\modelagem e catalogo\diagrama_er.png)

## Tabelas e grãos

| Camada | Tabela | Grão |
|---|---|---|
| bronze | `cno`, `cno_areas`, `dtb`, `estimativa_populacional` | cópia fiel dos arquivos originais (nomes de colunas normalizados) |
| silver | `cno`, `cno_areas`, `municipios`, `populacao_estimada` | limpo/validado/deduplicado; 1 linha por registro válido |
| gold | `dim_data` | 1 linha por dia (1990–2030) |
| gold | `dim_municipio` | 1 linha por município |
| gold | `dim_situacao` | 1 linha por situação (5 códigos) |
| gold | `dim_area` | 1 linha por combinação categoria × destinação × tipo de obra × tipo de área × complementar |
| gold | `fato_obras` | **1 linha por obra × área declarada** |
| gold | `fato_populacao` | 1 linha por município × ano (1991–2025) |

## Chaves e relacionamentos

- **Surrogate keys (SKs):** `sk_*` inteiras, determinísticas; `dim_data.sk_data` = `AAAAMMDD`.
- **Role-playing de `dim_data`:** `fato_obras` referencia a mesma dimensão de tempo duas vezes (`sk_data_inicio`, `sk_data_situacao`).
- **Integração geográfica:**
  - `fato_obras` → `dim_municipio` via **`codigo_tom`** (4 dígitos, padrão SIAFI — o CNO informa o código TOM).
  - `fato_populacao` → `dim_municipio` via **`codigo_municipio`** (IBGE, 7 dígitos).
- **Dimensões degeneradas:** `fato_obras.unidade_de_medida`; `fato_populacao.ano`.

## Camadas medalhão

O pipeline segue a arquitetura medalhão: **bronze** (dado como veio, com metadados) → **silver** (limpo, validado, padronizado) → **gold** (modelado para responder as perguntas). Detalhes do fluxo: tópico [Pipeline de Dados](../preparacao/README.md) e notebooks em `ETL/notebooks/`.

## Catálogo de dados

O catálogo (descrição, domínio e linhagem por campo) está transcrito por domínio, espelhando os dicionários em `ETL/catalogo/*.py`, e é aplicado nas tabelas via `add_column_comments` (`COMMENT` de coluna do Delta — visível no Unity Catalog / `DESCRIBE TABLE`). Cada tabela também recebe um **comentário descritivo** (camada, grão e linhagem) via `add_table_comment` (`ALTER TABLE ... SET TBLPROPERTIES ('comment' = ...)`, visível no Explorer / `DESCRIBE TABLE EXTENDED`).

## Evidências

> Prints a inserir:
> - [ ] Unity Catalog Explorer (tabelas de `workspace.bronze/silver/gold`).
> - [ ] `DESCRIBE TABLE` mostrando os comentários de coluna (catálogo aplicado).