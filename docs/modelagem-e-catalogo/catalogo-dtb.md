# Catálogo de Dados — DTB / Municípios (IBGE)

> [← Voltar para o README do tópico](README.md)

> Transcrito de `ETL/catalogo/divisao_territorial_brasileira.py`.
> Linhagem geral: `DTB_2025.zip` (FTP IBGE) → ODS no Volume → `bronze.dtb` → `silver.municipios` (+ enriquecimento TOM) → `gold.dim_municipio`.

---

## Bronze

### `workspace.bronze.dtb` — Divisão Territorial Brasileira (cópia fiel do `.ods`)

> **Comentário da tabela:** Camada bronze — cópia fiel do relatório `RELATORIO_DTB_BRASIL_2025_MUNICIPIOS.ods` (IBGE, Divisão Territorial Brasileira 2025). Grão: 1 linha por município. Colunas apenas normalizadas.

| Coluna | Descrição e domínio |
|---|---|
| `uf` | Código IBGE da UF (2 dígitos). Domínio: 11 a 53. *Header original: UF — contém CÓDIGO, não a sigla.* |
| `nome_uf` | Nome da UF (ex.: São Paulo, Bahia). 27 valores distintos. |
| `regiao_geografica_intermediaria` | Código da Região Geográfica Intermediária (4 dígitos). Domínio: 1101 a 5301. |
| `nome_regiao_geografica_intermediaria` | Nome da Região Geográfica Intermediária. |
| `regiao_geografica_imediata` | Código da Região Geográfica Imediata (6 dígitos). Domínio: 110001 a 530010. |
| `nome_regiao_geografica_imediata` | Nome da Região Geográfica Imediata. |
| `municipio` | Código do município SEM dígito verificador (6 dígitos). Uso apenas para validação; PK oficial é `codigo_municipio_completo`. |
| `codigo_municipio_completo` | Código IBGE do município COM DV (7 dígitos). Domínio: 1100015 a 5300108. **PK do relatório.** |
| `nome_municipio` | Nome oficial do município. |

_Evidência — comentários de coluna aplicados via `add_column_comments` no Databricks:_

![Comentários aplicados — `workspace.bronze.dtb`](../evidencias/modelagem%20e%20catalogo/comentarios_bronze_dtb.png)

---

## Silver

### `workspace.silver.municipios` — municípios limpos + enriquecidos com código TOM

> **Comentário da tabela:** Camada silver — municípios do IBGE limpos, validados (PK de 7 dígitos), deduplicados por código IBGE e enriquecidos com código TOM (SIAFI/Tesouro, via cidade-ibge-tom). Grão: 1 linha por município.

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `codigo_municipio` | Código IBGE com DV — 7 dígitos, string com zeros à esquerda. **PK.** Domínio: `^[0-9]{7}$` | `bronze.dtb.codigo_municipio_completo` |
| `codigo_uf` | Código IBGE da UF (2 dígitos, string pad). Domínio: '11' a '53' | `bronze.dtb.uf` |
| `sigla_uf` | Sigla da UF (mapa oficial IBGE — não vem no arquivo). Domínio: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO | mapa IBGE |
| `nome_uf` | Nome da UF (trim; casing preservado) | `bronze.dtb.nome_uf` |
| `codigo_regiao_geografica_intermediaria` | Código da Região Intermediária (4 dígitos, string pad). Ex.: '3101' | `bronze.dtb.regiao_geografica_intermediaria` |
| `nome_regiao_geografica_intermediaria` | Nome da Região Intermediária (trim) | `bronze.dtb.nome_regiao_geografica_intermediaria` |
| `codigo_regiao_geografica_imediata` | Código da Região Imediata (6 dígitos, string pad). Ex.: '310001' | `bronze.dtb.regiao_geografica_imediata` |
| `nome_regiao_geografica_imediata` | Nome da Região Imediata (trim) | `bronze.dtb.nome_regiao_geografica_imediata` |
| `nome_municipio` | Nome oficial do município (trim; casing original IBGE) | `bronze.dtb.nome_municipio` |
| `codigo_tom` | Código TOM (4 dígitos, SIAFI/Tesouro). Pode ser nulo para códigos ausentes na base. Domínio: '0101' a '9701' (São Paulo = '7107') | **enriquecimento** via `cidade-ibge-tom` (MIT) a partir de `codigo_municipio`; base: lista oficial SIAFI (Tesouro Transparente) |

_Evidência — comentários de coluna aplicados via `add_column_comments` no Databricks:_

![Comentários aplicados — `workspace.silver.municipios`](../evidencias/modelagem%20e%20catalogo/comentarios_silver_municipios.png)

---

## Gold

### `workspace.gold.dim_municipio` — dimensão município (localização)

> **Comentário da tabela:** Camada gold — dimensão conformada de município (star schema). Grão: 1 linha por município (SCD tipo 1, versão corrente). Permite joins por `codigo_municipio` (IBGE) ou `codigo_tom` (bases RFB, ex.: CNO).

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `sk_municipio` | Surrogate Key (int sequencial ordenada por `codigo_municipio`). **PK** | gerada |
| `codigo_municipio` | **Natural Key:** código IBGE com DV (7 dígitos, string) | `silver.municipios.codigo_municipio` |
| `codigo_tom` | Código TOM (4 dígitos, SIAFI). Permite joins com bases da RFB que usam TOM (ex.: CNO/CNPJ) | `silver.municipios.codigo_tom` |
| `nome_municipio` | Nome oficial do município | `silver.municipios.nome_municipio` |
| `codigo_uf` | Código IBGE da UF (2 dígitos). FK lógica para eventual `dim_uf` | `silver.municipios.codigo_uf` |
| `sigla_uf` | Sigla da UF (2 letras) | `silver.municipios.sigla_uf` |
| `nome_uf` | Nome da UF | `silver.municipios.nome_uf` |
| `codigo_regiao_geografica_intermediaria` | Código da Região Intermediária (4 dígitos) | `silver.municipios` |
| `nome_regiao_geografica_intermediaria` | Nome da Região Intermediária | `silver.municipios` |
| `codigo_regiao_geografica_imediata` | Código da Região Imediata (6 dígitos) | `silver.municipios` |
| `nome_regiao_geografica_imediata` | Nome da Região Imediata | `silver.municipios` |

_Evidência — comentários de coluna aplicados via `add_column_comments` no Databricks:_

![Comentários aplicados — `workspace.gold.dim_municipio`](../evidencias/modelagem%20e%20catalogo/comentarios_gold_dim_municipio.png)