# Catálogo de Dados — CNO (Cadastro Nacional de Obras)

> [← Voltar para o README do tópico](README.md)

> Transcrito de `ETL/catalogo/cadastro_nacional_obras.py`. Domínios oficiais (código → descrição) na seção final.
> Linhagem geral: CSV `dados.gov.br` (RFB) → `bronze` → `silver` → `gold` (dimensions + fato).

---

## Bronze

### `workspace.bronze.cno` — cadastro das obras (cópia fiel do `cno.csv`)

> **Comentário da tabela:** Camada bronze — cópia fiel do arquivo `cno.csv` do Cadastro Nacional de Obras (RFB, dados.gov.br). Grão: 1 linha por obra. Colunas apenas normalizadas (sem transformações de negócio).

| Coluna | Descrição e domínio |
|---|---|
| `cno` | Número do CNO |
| `codigo_do_pais` | Código do país |
| `nome_do_pais` | Nome do país |
| `data_de_inicio` | Data de início da obra (AAAA-MM-DD) |
| `data_de_inicio_da_responsabilidade` | Data de início da responsabilidade da obra (AAAA-MM-DD) |
| `data_de_registro` | Data de registro (AAAA-MM-DD) |
| `cno_vinculado` | Número da inscrição vinculada da obra |
| `cep` | Número do CEP (somente Brasil) |
| `ni_do_responsavel` | NI do responsável pela obra (CPF: campo em branco) |
| `qualificacao_do_responsavel` | 0053-Construtora; 0057-Dono da Obra; 0064-Incorporador; 0070-Proprietário; 0109-Consórcio; 0110-Construção em nome coletivo; 0111-Sociedade Líder de Consórcio |
| `nome` | Nome da obra |
| `codigo_do_municipio` | Código do município (TOM) |
| `nome_do_municipio` | Nome do município |
| `tipo_de_logradouro` | Tipo de logradouro |
| `logradouro` | Logradouro |
| `numero_do_logradouro` | Número do logradouro |
| `bairro` | Bairro |
| `estado` | Estado |
| `caixa_postal` | Caixa postal no exterior |
| `complemento` | Complemento do endereço |
| `unidade_de_medida` | Unidade de medida da obra |
| `area_total` | Valor da área total da obra |
| `situacao` | 01-NULA; 02-ATIVA; 03-SUSPENSA; 14-PARALISADA; 15-ENCERRADA |
| `data_da_situacao` | Data da situação da obra (AAAA-MM-DD) |
| `nome_empresarial` | Nome empresarial do responsável (pessoa física: campo em branco) |
| `codigo_de_localizacao` | Código da localização |

### `workspace.bronze.cno_areas` — áreas declaradas de cada obra (cópia fiel do `cno_areas.csv`)

> **Comentário da tabela:** Camada bronze — cópia fiel do arquivo `cno_areas.csv` do Cadastro Nacional de Obras (RFB, dados.gov.br). Grão: 1 linha por área declarada de uma obra (uma obra pode ter N áreas). Colunas apenas normalizadas.

| Coluna | Descrição e domínio |
|---|---|
| `cno` | Número do CNO |
| `categoria` | 0-Obra Nova; 1-Acréscimo; 2-Reforma; 3-Demolição; 4-Existente |
| `destinacao` | 0-Residencial unifamiliar; 1-Residencial multifamiliar; 2-Comercial salas e lojas; 3-Edifício de Garagens; 4-Galpão industrial; 5-Casa popular; 6-Conjunto habitacional popular |
| `tipo_de_obra` | 0-Alvenaria; 1-Madeira; 2-Mista |
| `tipo_de_area` | P-Principal; C-Complementar |
| `tipo_de_area_complementar` | 0-Quadra Esportiva e Poliesportiva; 1-Estacionamento Térreo; 2-Piscina; 3-Área Complementar do Posto de Gasolina |
| `metragem` | Metragem da área |

---

## Silver

### `workspace.silver.cno` — obras limpas e validadas

> **Comentário da tabela:** Camada silver — obras do Cadastro Nacional de Obras limpas, validadas e deduplicadas por `cno` (mantém a situação mais recente). Grão: 1 linha por obra. Regras: datas válidas, município TOM com registro em `silver.municipios`, unidade de medida `m²`, área total ≥ 0 e situação no domínio oficial RFB.

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `cno` | Número do CNO (inscrição da obra). **PK natural** | `bronze.cno.cno` (trim) |
| `data_de_inicio` | Data de início da obra (date, AAAA-MM-DD) | `bronze.cno.data_de_inicio`; inválidos/nulos descartados |
| `codigo_do_municipio` | Código TOM do município (SIAFI, 4 dígitos com pad à esquerda), normalizado e validado | `bronze.cno.codigo_do_municipio`; validado contra `silver.municipios.codigo_tom` (enriquecimento cidade-ibge-tom/SIAFI); sem correspondência é descartado |
| `unidade_de_medida` | Unidade de medida da área da obra — **somente `m²` aceita**; `km` e `,m2` (erros de digitação) são descartados | `bronze.cno.unidade_de_medida` (trim); regra definida na análise de qualidade (`qualidade/cadastro_nacional_obras.ipynb`) |
| `area_total` | Área total da obra (double, ≥ 0) | `bronze.cno.area_total` (cast numérico); nulos/negativos descartados |
| `situacao` | Código da situação: 01-NULA; 02-ATIVA; 03-SUSPENSA; 14-PARALISADA; 15-ENCERRADA | `bronze.cno.situacao`; fora do domínio descartado |
| `data_da_situacao` | Data da situação da obra (date, AAAA-MM-DD) | `bronze.cno.data_da_situacao`; inválidos/nulos descartados |

### `workspace.silver.cno_areas` — áreas limpas e validadas

> **Comentário da tabela:** Camada silver — áreas declaradas das obras, com textos dos domínios oficiais RFB validados e metragem ≥ 0. Grão: 1 linha por área declarada (uma obra pode ter N áreas).

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `cno` | Número do CNO (inscrição da obra). **FK para silver.cno** | `bronze.cno_areas.cno` |
| `categoria` | Texto oficial: 'Obra Nova'; 'Acréscimo'; 'Reforma'; 'Demolição'; 'Existente' | `bronze.cno_areas.categoria`; fora do domínio descartado |
| `destinacao` | Texto oficial: 'Residencial unifamiliar'; 'Residencial multifamiliar'; 'Comercial salas e lojas'; 'Edifício de Garagens'; 'Galpão industrial'; 'Casa popular'; 'Conjunto habitacional popular' | `bronze.cno_areas.destinacao`; fora do domínio descartado |
| `tipo_de_obra` | 'Alvenaria'; 'Madeira'; 'Mista' | `bronze.cno_areas.tipo_de_obra`; fora do domínio descartado |
| `tipo_de_area` | 'Principal'; 'Complementar' | `bronze.cno_areas.tipo_de_area`; fora do domínio descartado |
| `tipo_de_area_complementar` | 'Quadra Esportiva e Poliesportiva'; 'Estacionamento Térreo'; 'Piscina'; 'Área Complementar do Posto de Gasolina'; pode ser nulo quando `tipo_de_area` = Principal | `bronze.cno_areas.tipo_de_area_complementar` (literal 'null' do CSV → null) |
| `metragem` | Metragem da área (double, ≥ 0) | `bronze.cno_areas.metragem` (conversão tolerante); nulos/negativos descartados |

---

## Gold

### `workspace.gold.dim_situacao` — dimensão situação da obra

> **Comentário da tabela:** Camada gold — dimensão da situação da obra (star schema). Grão: 1 linha por código de situação oficial RFB (01-NULA a 15-ENCERRADA). Referenciada pela `fato_obras` via `sk_situacao`.

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `sk_situacao` | Surrogate Key (int sequencial ordenada por código). **PK** | gerada |
| `codigo_situacao` | Código da situação (**NK**): 01-NULA; 02-ATIVA; 03-SUSPENSA; 14-PARALISADA; 15-ENCERRADA | `silver.cno.situacao` |
| `descricao` | Descrição decodificada via domínio oficial RFB | domínio RFB |

### `workspace.gold.dim_area` — dimensão perfil da área declarada

> **Comentário da tabela:** Camada gold — dimensão de combinação do perfil das áreas declaradas (star schema). Grão: 1 linha por combinação categoria × destinação × tipo de obra × tipo de área × tipo complementar. Referenciada pela `fato_obras` via `sk_area`.

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `sk_area` | Surrogate Key (int sequencial). **PK**. Grão: combinação categoria × destinação × tipo de obra × tipo de área × complementar | gerada |
| `categoria` | Texto oficial da categoria | `silver.cno_areas.categoria` |
| `categoria_codigo` | Código RFB derivado do texto: 0-Obra Nova; 1-Acréscimo; 2-Reforma; 3-Demolição; 4-Existente | domínio RFB |
| `destinacao` | Texto oficial da destinação | `silver.cno_areas.destinacao` |
| `destinacao_codigo` | Código RFB da destinação (0 a 6) | domínio RFB |
| `tipo_de_obra` | Texto oficial do tipo de obra | `silver.cno_areas.tipo_de_obra` |
| `tipo_de_obra_codigo` | Código RFB: 0-Alvenaria; 1-Madeira; 2-Mista | domínio RFB |
| `tipo_de_area` | 'Principal' ou 'Complementar' | `silver.cno_areas.tipo_de_area` |
| `tipo_de_area_codigo` | Código RFB: P-Principal; C-Complementar | domínio RFB |
| `tipo_de_area_complementar` | Texto oficial do tipo complementar; nulo quando não aplicável | `silver.cno_areas.tipo_de_area_complementar` |
| `tipo_de_area_complementar_codigo` | Código RFB (0 a 3); nulo quando não aplicável | domínio RFB |

### `workspace.gold.fato_obras` — fato de obras (grão: obra × área)

> **Comentário da tabela:** Camada gold — fato de obras (star schema). Grão: 1 linha por obra × área declarada (obras iniciadas a partir de 1990). Medidas: `area_total` e `metragem`. Dimensões: `dim_data` (role-playing: data de início e da situação), `dim_situacao`, `dim_municipio` (via código TOM) e `dim_area`.

| Coluna | Descrição e domínio | Linhagem |
|---|---|---|
| `cno` | Número do CNO (**NK**). A fato repete a obra por área declarada | `silver.cno` |
| `sk_data_inicio` | **SK role-playing** de `gold.dim_data` para `data_de_inicio` (int AAAAMMDD, determinística) | `silver.cno.data_de_inicio` |
| `sk_data_situacao` | **SK role-playing** de `gold.dim_data` para `data_da_situacao` (int AAAAMMDD) | `silver.cno.data_da_situacao` |
| `sk_situacao` | **FK** para `gold.dim_situacao` | `silver.cno.situacao` |
| `sk_municipio` | **FK** para `gold.dim_municipio`. Join por código TOM: `silver.cno.codigo_do_municipio` (pad 4) = `dim_municipio.codigo_tom` | `silver.cno.codigo_do_municipio` |
| `sk_area` | **FK** para `gold.dim_area` (perfil da área declarada) | `silver.cno_areas` |
| `unidade_de_medida` | Unidade de medida (dimensão degenerada) | `silver.cno.unidade_de_medida` |
| `area_total` | **Medida:** área total da obra (double), repetida por linha de área | `silver.cno.area_total` |
| `metragem` | **Medida:** metragem da área declarada (double), no grão obra × área | `silver.cno_areas.metragem` |

---

## Domínios oficiais (código → descrição, RFB)

| Domínio | Valores |
|---|---|
| `situacao` | 01-NULA; 02-ATIVA; 03-SUSPENSA; 14-PARALISADA; 15-ENCERRADA |
| `categoria` | 0-Obra Nova; 1-Acréscimo; 2-Reforma; 3-Demolição; 4-Existente |
| `destinacao` | 0-Residencial unifamiliar; 1-Residencial multifamiliar; 2-Comercial salas e lojas; 3-Edifício de Garagens; 4-Galpão industrial; 5-Casa popular; 6-Conjunto habitacional popular |
| `tipo_de_obra` | 0-Alvenaria; 1-Madeira; 2-Mista |
| `tipo_de_area` | P-Principal; C-Complementar |
| `tipo_de_area_complementar` | 0-Quadra Esportiva e Poliesportiva; 1-Estacionamento Térreo; 2-Piscina; 3-Área Complementar do Posto de Gasolina |