# Catálogo de Dados — Dimensão de data (`dim_data`)

> [← Voltar para o README do tópico](README.md)

> Transcrito de `ETL/catalogo/dimensao_data.py`.
> **Fonte:** nenhuma fonte externa — calendário gerado proceduralmente.
> **Linhagem:** geração determinística em memória (sequence de datas diárias) → `gold.dim_data`.
>
> A dimensão é **conformada e reusada por todas as fatos** via role-playing (ex.: `fato_obras.sk_data_inicio` e `fato_obras.sk_data_situacao`).

---

## `workspace.gold.dim_data`

> **Comentário da tabela:** Camada gold — dimensão conformada de data (calendário). Grão: 1 linha por dia, de 1990-01-01 a 2030-12-31. Gerada proceduralmente (sem fonte externa); reusada pelas fatos via role-playing.

| Coluna | Descrição e domínio |
|---|---|
| `sk_data` | Surrogate Key: inteiro `AAAAMMDD` (ex.: 20250815). **PK.** Determinística (estável entre execuções). |
| `data` | Data do calendário (date). Grão: 1 linha por dia. |
| `ano` | Ano (int). Domínio: 1990 a 2030. |
| `semestre` | Semestre (int). Domínio: 1 a 2. |
| `trimestre` | Trimestre (int). Domínio: 1 a 4. |
| `bimestre` | Bimestre (int). Domínio: 1 a 6. |
| `mes` | Mês (int). Domínio: 1 a 12. |
| `nome_mes` | Nome do mês em português (Janeiro a Dezembro). |
| `dia` | Dia do mês (int). Domínio: 1 a 31. |
| `dia_semana` | Número do dia na semana. Convenção: 1=Domingo a 7=Sábado. |
| `nome_dia_semana` | Nome do dia da semana em português (Domingo a Sábado). |
| `semana_do_ano` | Semana do ano ISO (int). Domínio: 1 a 53. |
| `ano_mes` | Ano-mês `'AAAA-MM'` (string) para agregações mensais. |
| `flag_fim_de_semana` | Booleano: true em sábado/domingo (útil para sazonalidade). |

_Evidência — comentários de coluna aplicados via `add_column_comments` no Databricks:_

![Comentários aplicados — `workspace.gold.dim_data`](../evidencias/modelagem%20e%20catalogo/comentarios_gold_dim_data.png)