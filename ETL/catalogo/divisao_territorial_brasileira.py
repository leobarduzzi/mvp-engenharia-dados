# Catálogo de dados DTB - Divisão Territorial Brasileira (IBGE)
#
# Fonte: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/23701-divisao-territorial-brasileira.html
# Arquivo origem: /Volumes/workspace/raw/IBGE/RELATORIO_DTB_BRASIL_2025_MUNICIPIOS.ods
#   (extraído de DTB_2025.zip - geoftp.ibge.gov.br/organizacao_do_territorio/divisao_territorial/2025/)
# Enriquecimento: código TOM derivado via biblioteca cidade-ibge-tom (MIT) ->
#   base estática da lista oficial de municípios do SIAFI
#   https://www.tesourotransparente.gov.br/ckan/dataset/lista-de-municipios-do-siafi
# Linhagem: download IBGE -> ODS no Volume (cabeçalho na linha 7) ->
#            bronze.dtb -> silver.municipios (+ enriquecimento TOM) -> gold.dim_municipio
#
# As chaves dos dicionários são os nomes de colunas após `normalizar_colunas`.

DTB_COMMENTS = {
    "uf": (
        "Código IBGE da Unidade da Federação (2 dígitos). "
        "Domínio: 11 a 53. Header original: UF — contém CÓDIGO, não a sigla."
    ),
    "nome_uf": "Nome da Unidade da Federação (ex.: São Paulo, Bahia). 27 valores distintos.",
    "regiao_geografica_intermediaria": (
        "Código da Região Geográfica Intermediária (4 dígitos: 2 da UF + 2 sequenciais). "
        "Domínio: 1101 a 5301. Header original: Região Geográfica Intermediária."
    ),
    "nome_regiao_geografica_intermediaria": (
        "Nome da Região Geográfica Intermediária. "
        "Header original: Nome Região Geográfica Intermediária."
    ),
    "regiao_geografica_imediata": (
        "Código da Região Geográfica Imediata (6 dígitos: 2 da UF + 4 sequenciais). "
        "Domínio: 110001 a 530010. Header original: Região Geográfica Imediata."
    ),
    "nome_regiao_geografica_imediata": (
        "Nome da Região Geográfica Imediata. "
        "Header original: Nome Região Geográfica Imediata."
    ),
    "municipio": (
        "Código do município SEM dígito verificador (6 dígitos). "
        "Domínio: 110001 a 530010. Uso apenas para validação; a PK oficial é codigo_municipio_completo."
    ),
    "codigo_municipio_completo": (
        "Código IBGE do município COM dígito verificador (7 dígitos: 6 base + 1 DV). "
        "Domínio: 1100015 a 5300108. PK do relatório. Header original: Código Município Completo."
    ),
    "nome_municipio": "Nome oficial do município. Header original: Nome_Município.",
}

SILVER_MUNICIPIOS_COMMENTS = {
    "codigo_municipio": (
        "Código IBGE do município com DV — 7 dígitos, string com zeros à esquerda preservados. "
        "PK. Derivado de bronze.dtb.codigo_municipio_completo. Domínio: ^[0-9]{7}$ (1100015 a 5300108)."
    ),
    "codigo_uf": (
        "Código IBGE da UF (2 dígitos, string pad). Derivado de bronze.dtb.uf. Domínio: '11' a '53'."
    ),
    "sigla_uf": (
        "Sigla da UF derivada de codigo_uf via mapa oficial IBGE (não vem no arquivo origem). "
        "Domínio: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO."
    ),
    "nome_uf": "Nome da UF (trim; casing preservado do origem). Derivado de bronze.dtb.nome_uf.",
    "codigo_regiao_geografica_intermediaria": (
        "Código da Região Geográfica Intermediária (4 dígitos, string pad). "
        "Derivado de bronze.dtb.regiao_geografica_intermediaria. Ex.: '3101'."
    ),
    "nome_regiao_geografica_intermediaria": (
        "Nome da Região Geográfica Intermediária (trim). Derivado de bronze.dtb.nome_regiao_geografica_intermediaria."
    ),
    "codigo_regiao_geografica_imediata": (
        "Código da Região Geográfica Imediata (6 dígitos, string pad). "
        "Derivado de bronze.dtb.regiao_geografica_imediata. Ex.: '310001'."
    ),
    "nome_regiao_geografica_imediata": (
        "Nome da Região Geográfica Imediata (trim). Derivado de bronze.dtb.nome_regiao_geografica_imediata."
    ),
    "nome_municipio": (
        "Nome oficial do município (trim; casing original do IBGE é mantido). "
        "Derivado de bronze.dtb.nome_municipio."
    ),
    "codigo_tom": (
        "Código TOM do município (4 dígitos, padrão SIAFI/Tesouro Nacional, string). "
        "Enriquecimento via biblioteca cidade-ibge-tom (MIT) a partir de codigo_municipio (IBGE); "
        "base: lista oficial de municípios do SIAFI — Tesouro Transparente. "
        "Pode ser nulo para códigos ausentes na base estática da biblioteca. "
        "Domínio: '0101' a '9701' (ex.: São Paulo = '7107')."
    ),
}

DIM_MUNICIPIO_COMMENTS = {
    "sk_municipio": (
        "Surrogate Key da dimensão (int sequencial, gerada ordenando por codigo_municipio). PK da dim."
    ),
    "codigo_municipio": (
        "Natural Key: código IBGE do município com DV (7 dígitos, string). Vem de silver.municipios.codigo_municipio."
    ),
    "codigo_tom": (
        "Código TOM do município (4 dígitos, string). Vem de silver.municipios.codigo_tom "
        "(enriquecimento via biblioteca cidade-ibge-tom — lista SIAFI/Tesouro). "
        "Permite joins diretos com bases da RFB que usam código TOM (ex.: CNO/CNPJ)."
    ),
    "nome_municipio": "Nome oficial do município. Vem de silver.municipios.nome_municipio.",
    "codigo_uf": "Código IBGE da UF (2 dígitos). FK lógica para eventual dim_uf. Vem de silver.municipios.codigo_uf.",
    "sigla_uf": "Sigla da UF (2 letras). Vem de silver.municipios.sigla_uf.",
    "nome_uf": "Nome da UF. Vem de silver.municipios.nome_uf.",
    "codigo_regiao_geografica_intermediaria": (
        "Código da Região Geográfica Intermediária (4 dígitos). Vem de silver.municipios."
    ),
    "nome_regiao_geografica_intermediaria": "Nome da Região Geográfica Intermediária. Vem de silver.municipios.",
    "codigo_regiao_geografica_imediata": (
        "Código da Região Geográfica Imediata (6 dígitos). Vem de silver.municipios."
    ),
    "nome_regiao_geografica_imediata": "Nome da Região Geográfica Imediata. Vem de silver.municipios.",
}
