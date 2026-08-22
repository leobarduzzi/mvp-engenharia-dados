# Metadados DTB - Divisão Territorial Brasileira (IBGE)
# Fonte: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/23701-divisao-territorial-brasileira.html
# Arquivo origem: /Volumes/workspace/raw/IBGE/RELATORIO_DTB_BRASIL_2025_MUNICIPIOS.ods (extraído de DTB_2025.zip)
# Linhagem: download IBGE -> /Volumes/workspace/raw/IBGE/RELATORIO_DTB_BRASIL_2025_MUNICIPIOS.ods (header na linha 7) -> bronze.dtb -> silver.municipios -> gold.dim_municipio
# Colunas confirmadas pelo usuário em 22/08/2026 (header linha 7 do .ods):
# UF | Nome_UF | Região Geográfica Intermediária | Nome Região Geográfica Intermediária | Região Geográfica Imediata | Nome Região Geográfica Imediata | Município | Código Município Completo | Nome_Município

DTB_COMMENTS = {
    "uf": "Código da Unidade da Federação com 2 dígitos (11 a 53). Header original: UF — contém CÓDIGO, não sigla",
    "nome_uf": "Nome da Unidade da Federação. Ex.: São Paulo, Bahia",
    "regiao_geografica_intermediaria": "Código da Região Geográfica Intermediária (4 dígitos: 2 UF + 2 seq). Ex.: 3101. Header original: Região Geográfica Intermediária",
    "nome_regiao_geografica_intermediaria": "Nome da Região Geográfica Intermediária. Header original: Nome Região Geográfica Intermediária",
    "regiao_geografica_imediata": "Código da Região Geográfica Imediata (6 dígitos: 2 UF + 4 seq). Ex.: 310001. Header original: Região Geográfica Imediata",
    "nome_regiao_geografica_imediata": "Nome da Região Geográfica Imediata. Header original: Nome Região Geográfica Imediata",
    "municipio": "Código do Município sem DV (5-6 dígitos, campo 'Município' no ODS). Usar apenas para validação; PK oficial é codigo_municipio_completo",
    "codigo_municipio_completo": "Código do Município IBGE com 7 dígitos (6 base + 1 DV). PK oficial. Domínio: 1100015 a 5300108. Header original: Código Município Completo",
    "nome_municipio": "Nome do Município. Header original: Nome_Município",
}

SILVER_MUNICIPIOS_COMMENTS = {
    "codigo_municipio": "Código Município IBGE 7 dígitos (string, preserva zero à esquerda, DV). PK. Derivado de codigo_municipio_completo. ^[0-9]{7}$",
    "codigo_uf": "Código UF 2 dígitos (de UF ou dos 2 primeiros dígitos do codigo_municipio). Domínio: 11-53",
    "sigla_uf": "Sigla UF (2 letras maiúsculas) derivada do código UF via mapa IBGE. Domínio: AC..TO (27 valores)",
    "nome_uf": "Nome UF padronizado (Title Case, trim)",
    "nome_municipio": "Nome Município (Title Case, trim, sem espaços duplos)",
}

DIM_MUNICIPIO_COMMENTS = {
    "sk_municipio": "Surrogate Key da dimensão (int sequencial, PK dim)",
    "codigo_municipio": "Código Município IBGE 7 dígitos (Natural Key, string)",
    "nome_municipio": "Nome Município (Title Case)",
    "codigo_uf": "Código UF 2 dígitos (FK lógica)",
    "sigla_uf": "Sigla UF (2 letras)",
    "nome_uf": "Nome UF",
}
