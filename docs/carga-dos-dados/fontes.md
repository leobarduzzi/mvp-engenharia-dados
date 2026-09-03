# Origem dos dados — detalhamento por fonte

> Complementa o [README](README.md) do tópico **Carga dos Dados**. Detalha a origem, o formato e a coleta de cada conjunto de dados.

---

## 1. CNO — Cadastro Nacional de Obras (RFB)

- **Portal / conjunto de dados:** [Cadastro Nacional de Obras](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-de-obras-cno) (dados.gov.br).
- **Área responsável:** RFB — Secretaria Especial da Receita Federal do Brasil (e-mail: ouvidoria.df@rfb.gov.br).
- **O que é:** banco de dados com informações cadastrais de obras de construção civil e seus responsáveis, usado para o cumprimento de obrigações tributárias e obtenção da certidão de regularidade fiscal da obra.
- **Licença:** Creative Commons Attribution.
- **Atualização:** diária.
- **Arquivos coletados (2):**
  | Arquivo | Conteúdo | Encoding | Formato |
  |---|---|---|---|
  | `cno.csv` | cadastro das obras | Windows-1252 | CSV (delimitador `,`) |
  | `cno_areas.csv` | áreas declaradas de cada obra (destinação, tipo, metragem) | Windows-1252 | CSV (delimitador `,`) |
- **Coleta:** download dos CSVs pelo portal e upload manual para `/Volumes/workspace/raw/cno/`.
- **Nota (limitação):** o download usa uma URL do portal, porém **não há documentação indicando que a URL é fixa/estável**. A coleta foi tratada como **snapshot manual** — conferir a URL a cada atualização.

## 2. DTB — Divisão Territorial Brasileira (IBGE)

- **Fonte:** [Divisão Territorial Brasileira — IBGE](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/23701-divisao-territorial-brasileira.html).
- **Coleta:** download de `DTB_2025.zip` no FTP do IBGE (`geoftp.ibge.gov.br/organizacao_do_territorio/divisao_territorial/2025/`), extração do arquivo `RELATORIO_DTB_BRASIL_2025_MUNICIPIOS.ods` e upload manual para `/Volumes/workspace/raw/IBGE/`.
- **Licença:** dados públicos IBGE — uso livre com citação da fonte.
- **Atualização:** anual (edição 2025; inclui o município Boa Esperança do Norte/MT).
- **Estrutura do arquivo:** planilha `.ods` com cabeçalho na linha 7 (índice `6`); colunas: UF (código), Nome_UF, Região Geográfica Intermediária, Nome Região Geográfica Intermediária, Região Geográfica Imediata, Nome Região Geográfica Imediata, Município, Código Município Completo, Nome_Município.
- **Nota:** a coluna `UF` contém o **código** da UF (11–53), não a sigla.

## 3. População por município (IBGE via Base dos Dados)

- **Fonte:** Base dos Dados — tabela `br_ibge_populacao.municipio` ([População Brasileira](https://basedosdados.org/dataset/d30222ad-7a5c-4778-a1ec-f0785371d1ca?table=0c279444-165b-41da-92cd-50fd7e66baa1)).
- **Origem do dado:** estimativas anuais do IBGE (referência 1º de julho; anos de censo/contagem usam o total recenseado: 1991, 2000, 2010, 2022).
- **Cobertura:** 1991 a 2025.
- **Licença:** CC-BY-4.0 (Base dos Dados / IBGE).
- **Arquivo coletado:** `br_ibge_populacao_municipio.csv` — UTF-8, header na 1ª linha: `ano, sigla_uf, id_municipio, populacao`.
- **Coleta:** download do CSV exportado da plataforma Base dos Dados e upload manual para `/Volumes/workspace/raw/basedosdados/`.

---

## Linhagem resumida (raw → bronze)

- CNO: `dados.gov.br` → `cno.csv`/`cno_areas.csv` → `workspace.bronze.cno` / `workspace.bronze.cno_areas`
- DTB: `DTB_2025.zip` (FTP IBGE) → `.ods` → `workspace.bronze.dtb`
- População: Base dos Dados → CSV → `workspace.bronze.estimativa_populacional`