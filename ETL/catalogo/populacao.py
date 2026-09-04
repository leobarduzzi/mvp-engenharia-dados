# Catálogo de dados POP - População por Município (IBGE via Base dos Dados)
#
# Fonte: Base dos Dados - tabela br_ibge_populacao.municipio
#   https://basedosdados.org/dataset/d30222ad-7a5c-4778-a1ec-f0785371d1ca?table=0c279444-165b-41da-92cd-50fd7e66baa1
# Dados: estimativas do total da população dos municípios com data de referência
#   em 1º de julho (anos de censo/contagem usam o total recenseado), IBGE.
# Cobertura temporal: 1991 a 2025 (anos de censo/contagem: 1991, 2000, 2010, 2022).
# Arquivo origem: /Volumes/workspace/raw/basedosdados/br_ibge_populacao_municipio.csv
#   (UTF-8; header: ano,sigla_uf,id_municipio,populacao)
# Licença: Base dos Dados (CC-BY-4.0) — republicação dos dados públicos do IBGE.
# Linhagem: download Base dos Dados -> CSV no Volume ->
#            bronze.estimativa_populacional -> silver.populacao_estimada
#            (validação contra silver.municipios) -> gold.fato_populacao
#
# As chaves dos dicionários são os nomes de colunas após `normalizar_colunas`.

BRONZE_ESTIMATIVA_POPULACAO_TABLE_COMMENT = (
    "Camada bronze — cópia fiel do arquivo br_ibge_populacao_municipio.csv "
    "(Base dos Dados / IBGE). Grão: 1 linha por município x ano (1991 a "
    "2025). Colunas apenas normalizadas."
)

SILVER_POPULACAO_TABLE_COMMENT = (
    "Camada silver — estimativas populacionais validadas, conciliadas com "
    "silver.municipios (código IBGE e sigla da UF) e deduplicadas por "
    "município x ano. Grão: 1 linha por município x ano (1991 a 2025)."
)

FATO_POPULACAO_TABLE_COMMENT = (
    "Camada gold — fato de snapshot periódico da população por município "
    "(star schema). Grão: 1 linha por município x ano (1991 a 2025). Medida: "
    "populacao. Dimensão: dim_municipio (via sk_municipio)."
)

BRONZE_ESTIMATIVA_POPULACAO_COMMENTS = {
    "ano": (
        "Ano de referência da população (AAAA). Header original: 'ano'. "
        "Domínio: 1991 a 2025 (estimativas IBGE, referência 1º de julho; "
        "anos de censo/contagem: 1991, 2000, 2010, 2022)."
    ),
    "sigla_uf": "Sigla da Unidade da Federação (2 letras). Header original: 'sigla_uf'. Domínio: 27 UFs.",
    "id_municipio": (
        "Código IBGE do município com DV (7 dígitos, string). Header original: 'id_municipio'. "
        "Domínio: ^[0-9]{7}$ (1100015 a 5300108)."
    ),
    "populacao": (
        "População residente no município no ano (int). Header original: 'populacao'. "
        "Estimativas anuais IBGE; anos de censo/contagem usam o total recenseado."
    ),
}

SILVER_POPULACAO_COMMENTS = {
    "codigo_municipio": (
        "Código IBGE do município com DV (7 dígitos, string). PK parcial (com ano). "
        "Derivado de bronze.id_municipio e validado contra silver.municipios.codigo_municipio; "
        "sem correspondência é descartado."
    ),
    "sigla_uf": (
        "Sigla da UF informada no arquivo origem. Campo de auditoria: "
        "divergente da sigla oficial (silver.municipios.sigla_uf) invalida a linha."
    ),
    "ano": "Ano de referência da população (int). Domínio: 1991 a 2025. Fora do intervalo/nulo é descartado.",
    "populacao": (
        "População residente estimada (long, > 0). Derivado de bronze.populacao "
        "com conversão tolerante; nulos/não positivos descartados."
    ),
}

FATO_POPULACAO_COMMENTS = {
    "sk_municipio": (
        "FK para gold.dim_municipio (localização). Join por codigo_municipio (IBGE 7 dígitos)."
    ),
    "codigo_municipio": (
        "Natural Key degenerada: código IBGE do município com DV (7 dígitos). Vem de silver.populacao_estimada."
    ),
    "ano": (
        "Dimensão degenerada: ano de referência da população (int). "
        "Grão da fato: 1 linha por município x ano (1991-2025)."
    ),
    "populacao": (
        "Medida: população residente (long). Vem de silver.populacao_estimada."
    ),
}
