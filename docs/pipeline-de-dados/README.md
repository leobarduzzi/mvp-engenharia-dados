# Pipeline de Dados (Etapa 4.4)

> Documento principal do tópico **"Pipeline de Dados"**.
> Detalhamento dos helpers reutilizáveis: [Helpers (`src/data_pipeline`)](helpers.md)

---

## Organização do pipeline

O pipeline foi **ramificado por domínio e por camada** (arquitetura medalhão): cada transformação relevante tem seu próprio notebook, seguindo o fluxo `bronze → silver → gold`. Isso mantém cada notebook curto, reprodutível e com responsabilidade única — em vez de um único notebook monolítico.

```
ETL/notebooks/
  divisao_territorial_brasileira/
    01_bronze_dtb.ipynb  →  02_silver_municipios.ipynb  →  03_gold_dim_municipio.ipynb
  dimensao_data/
    01_gold_dim_data.ipynb
  populacao/
    01_bronze_populacao.ipynb  →  02_silver_populacao.ipynb  →  03_gold_fato_populacao.ipynb
  cadastro_nacional_obras/
    01_bronze_cno.ipynb / 01_bronze_cno_areas.ipynb
    02_silver_cno.ipynb / 02_silver_cno_areas.ipynb
    03_gold_dim_area.ipynb / 03_gold_dim_situacao.ipynb
    04_gold_fato_obras.ipynb
```

## Dependências e ordem de execução

| Ordem | Etapa | Depende de | Gera |
|---|---|---|---|
| 1 | DTB (bronze → silver → gold) | — | `silver.municipios`, `gold.dim_municipio` |
| 2 | `gold.dim_data` | — | calendário 1990–2030 |
| 3 | População (bronze → silver → gold) | `silver.municipios` (validação), `gold.dim_municipio` | `gold.fato_populacao` |
| 4 | CNO (bronze → silver → gold) | `silver.municipios` (validação TOM), `dim_data`, `dim_municipio` | `gold.fato_obras` |

> A camada de **municípios (DTB)** é a fundação geográfica: valida o CNO (por código TOM) e a população (por código IBGE).

## Transformações e conciliações principais

- **`silver.municipios`** — enriquecimento: deriva o **código TOM** (SIAFI/Tesouro) a partir do código IBGE via biblioteca `cidade-ibge-tom` (MIT) — chave que integra as bases da RFB (CNO) com a geografia IBGE.
- **`silver.cno`** — conciliação de município: o CNO informa o código no **padrão TOM**; valida contra `silver.municipios.codigo_tom` (com pad de 4 dígitos) e descarta os sem correspondência. Diagnóstico auxiliar compara adesão TOM vs IBGE. **Deduplicação** por `cno` mantendo a situação mais recente (`data_da_situacao`).
- **`silver.cno_areas`** — validação de domínios textuais oficiais (categoria, destinação, tipo de obra/área); literal `'null'` do CSV normalizado para nulo.
- **`silver.populacao_estimada`** — conciliação por `codigo_municipio` (IBGE 7 dígitos) + **auditoria** da `sigla_uf` (divergência da sigla oficial invalida a linha).
- **`gold.fato_obras`** — `inner join` entre obra e suas áreas declaradas (grão obra × área); **role-playing** de `dim_data` (início e situação); lookups de SK por código de situação, código TOM e combinação **null-safe** de 5 atributos na `dim_area`.
- **`gold.fato_populacao`** — join de `silver.populacao_estimada` com `dim_municipio` por `codigo_municipio`.

## Helpers reutilizáveis

Toda a lógica de leitura, escrita, normalização e qualidade está em **`src/data_pipeline`** — os notebooks apenas orquestram, chamando os helpers (nenhuma lógica duplicada). Detalhamento: [Helpers](helpers.md).

## Persistência e evidências

- Toda persistência é **Delta** via `save_table` (`saveAsTable`), seguida de `add_column_comments` (catálogo aplicado na própria tabela).
- Referência aos scripts: [notebooks em `ETL/notebooks/`](../../ETL/notebooks/).

> Prints a inserir:
> - [ ] Explorer mostrando as tabelas persistidas em `workspace.bronze/silver/gold`.
> - [ ] `SELECT count(*)` de cada tabela final (evidência da carga).