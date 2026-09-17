# Contexto de Negócios e Perguntas

> Documento principal do tópico **"Contexto de Negócios e Perguntas"**.
> Detalhamentos: [Perguntas de negócio](perguntas.md) · [Definições operacionais](definicoes.md)

---

## Problema

O **Cadastro Nacional de Obras (CNO)**, mantido pela Receita Federal do Brasil (RFB), registra, para fins tributários, as obras de construção civil e as áreas que as compõem — incluindo a **destinação** da área (ex.: residencial unifamiliar, casa popular) e a respectiva **metragem**.

Ao combinar esse cadastro com a **divisão territorial** (IBGE) e as **estimativas populacionais** (IBGE via Base dos Dados), é possível traçar um panorama do **tamanho das casas populares e unifamiliares** no Brasil e responder as perguntas de negócio:

1. A **área média das casas** variou ao longo do tempo?
2. O **porte populacional** do município (e da sua região geográfica imediata) se relaciona com a **área construída** dessas casas?
3. Obras menores têm mais chance de ficarem **paralisadas ou nulas**?


## Tema

**Panorama do tamanho das casas populares e unifamiliares conforme o Cadastro Nacional de Obras (CNO).**

## Origem dos dados brutos (resumo)

| Fonte | Tabela bronze | Principais colunas | Licença |
|---|---|---|---|
| CNO — Cadastro Nacional de Obras ([dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-de-obras-cno)) | `workspace.bronze.cno` | cno, data_de_inicio, codigo_do_municipio, unidade_de_medida, area_total, situacao, data_da_situacao | Creative Commons Attribution (RFB) |
| CNO — Áreas declaradas ([dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-de-obras-cno)) | `workspace.bronze.cno_areas` | cno, categoria, destinacao, tipo_de_obra, tipo_de_area, tipo_de_area_complementar, metragem | Creative Commons Attribution (RFB) |
| DTB — Divisão Territorial Brasileira ([IBGE](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/23701-divisao-territorial-brasileira.html)) | `workspace.bronze.dtb` | UF, município, código do município completo, regiões geográficas intermediária e imediata | Dados públicos IBGE (citação da fonte) |
| Estimativas populacionais por município ([Base dos Dados](https://basedosdados.org/dataset/d30222ad-7a5c-4778-a1ec-f0785371d1ca?table=0c279444-165b-41da-92cd-50fd7e66baa1)) | `workspace.bronze.estimativa_populacional` | ano, sigla_uf, id_municipio, populacao | CC-BY-4.0 (Base dos Dados / IBGE) |

> O detalhamento completo de cada coluna (descrição, domínio, linhagem) está no [Catálogo de Dados](../../ETL/catalogo/), transcrito no tópico [Modelagem e Catálogo](../modelagem-e-catalogo/README.md).

## Perguntas de negócio (resumo)

| # | Pergunta | Status |
|---|---|---|
| P1 | Houve variação no tempo da área média das casas (unifamiliares e populares)? | Não respondida (não conclusiva) |
| P2 | O tamanho populacional do município se relaciona com a área construída? E o tamanho populacional da região geográfica imediata? | Respondida (com ressalvas) |
| P3 | Qual a distribuição das situações (ativa, paralisada, encerrada etc.) por porte de obra? Obras menores têm mais chance de ficarem paralisadas/nulas? | Respondida |


## Decisões de escopo

Para responder às perguntas com consistência, são necessárias definições explícitas de escopo (o que conta como "casa", qual métrica de área, quais filtros). As decisões tomadas estão registradas em [Definições operacionais](definicoes.md).