# Catálogo de Dados — População (IBGE via Base dos Dados)

> [← Voltar para o README do tópico](README.md)

> Transcrito de `ETL/catalogo/populacao.py`.
> Linhagem geral: Base dos Dados → CSV no Volume → `bronze.estimativa_populacional` → `silver.populacao_estimada` (validação contra `silver.municipios`) → `gold.fato_populacao`.

---

## Bronze

### `workspace.bronze.estimativa_populacional` — estimativas anuais por município (cópia fiel do CSV)

> **Comentário da tabela:** Camada bronze — cópia fiel do arquivo `br_ibge_populacao_municipio.csv` (Base dos Dados / IBGE). Grão: 1 linha por município × ano (1991 a 2025). Colunas apenas normalizadas.

| Coluna | Descrição e domínio |
|---|---|
| `ano` | Ano de referência (AAAA). Domínio: 1991 a 2025 (estimativas IBGE, referência 1º de julho; censo/contagem: 1991, 2000, 2010, 2022). |
| `sigla_uf` | Sigla da UF (2 letras). Domínio: 27 UFs. |
| `id_municipio` | Código IBGE do município com DV (7 dígitos, string). Domínio: `^[0-9]{7}$` (1100015 a 5300108). |
| `populacao` | População residente no município no ano (int). |

---

## Silver

### `workspace.silver.populacao_estimada` — população validada

> **Comentário da tabela:** Camada silver — estimativas populacionais validadas, conciliadas com `silver.municipios` (código IBGE e sigla da UF) e deduplicadas por município × ano. Grão: 1 linha por município × ano (1991 a 2025).

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `codigo_municipio` | Código IBGE com DV (7 dígitos, string). **PK parcial (com `ano`)** | `bronze.id_municipio`, validado contra `silver.municipios.codigo_municipio`; sem correspondência é descartado |
| `sigla_uf` | Sigla da UF do arquivo origem. **Campo de auditoria:** divergente da sigla oficial (`silver.municipios.sigla_uf`) invalida a linha | `bronze.sigla_uf` |
| `ano` | Ano de referência (int). Domínio: 1991 a 2025. Fora do intervalo/nulo é descartado | `bronze.ano` |
| `populacao` | População estimada (long, > 0) | `bronze.populacao` (conversão tolerante); nulos/não positivos descartados |

---

## Gold

### `workspace.gold.fato_populacao` — fato de população (grão: município × ano)

> **Comentário da tabela:** Camada gold — fato de snapshot periódico da população por município (star schema). Grão: 1 linha por município × ano (1991 a 2025). Medida: `populacao`. Dimensão: `dim_municipio` (via `sk_municipio`).

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `sk_municipio` | **FK** para `gold.dim_municipio`. Join por `codigo_municipio` (IBGE 7 dígitos) | `silver.populacao_estimada.codigo_municipio` |
| `codigo_municipio` | Natural Key degenerada: código IBGE com DV (7 dígitos) | `silver.populacao_estimada.codigo_municipio` |
| `ano` | Dimensão degenerada: ano de referência (int). Grão: município × ano (1991–2025) | `silver.populacao_estimada.ano` |
| `populacao` | **Medida:** população residente (long) | `silver.populacao_estimada.populacao` |