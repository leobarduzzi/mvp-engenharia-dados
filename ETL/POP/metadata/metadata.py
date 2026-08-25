# Catálogo de dados POP - Estimativas de População Residente (IBGE/SIDRA)
#
# Fonte: SIDRA tabela 6579 - População residente estimada
#   https://sidra.ibge.gov.br/pesquisa/estimapop/tabelas
#   (exportação CSV, todos os anos disponíveis: 2001 a 2025, nível município)
# Arquivo origem: /Volumes/workspace/raw/IBGE/estimativa_populacional_6579.csv
#   (UTF-8 com BOM; 1ª linha = título da tabela, 2ª linha = cabeçalho)
# Licença: dados públicos IBGE — reutilização autorizada com citação da fonte
#   (IBGE, Estimativas de População / SIDRA).
# Linhagem: download SIDRA -> CSV no Volume ->
#            bronze.estimativa_populacional -> silver.populacao_estimada
#            (validação contra silver.municipios) -> gold.fato_populacao
#
# As chaves dos dicionários são os nomes de colunas após `normalizar_colunas`.

BRONZE_ESTIMATIVA_POPULACAO_COMMENTS = {
    "codigo_municipio": (
        "Código IBGE do município com DV (7 dígitos). Header original do SIDRA: 'Cód.'."
    ),
    "municipio": (
        "Nome do município seguido da sigla da UF entre parênteses "
        "(ex.: \"Alta Floresta D'Oeste (RO)\"). Header original: 'Município'."
    ),
    "ano": "Ano de referência da estimativa (AAAA). Header original: 'Ano'. Domínio: 2001 a 2025.",
    "variavel": (
        "Nome da variável SIDRA — constante 'População residente estimada (Pessoas)' nesta extração. "
        "Usado para conferência; não segue para a silver."
    ),
    "valor": "Valor da variável: população residente estimada (inteiro). Última coluna sem nome no header.",
}

SILVER_POPULACAO_COMMENTS = {
    "codigo_municipio": (
        "Código IBGE do município com DV (7 dígitos, string). PK parcial (com ano). "
        "Validado contra silver.municipios.codigo_municipio; sem correspondência é descartado."
    ),
    "nome_municipio": (
        "Nome do município extraído do campo origem (sem o sufixo '(UF)'). "
        "Referência/auditoria; nome oficial vive em silver.municipios."
    ),
    "sigla_uf_informada": (
        "Sigla da UF extraída dos parênteses do campo origem. Campo de auditoria: "
        "divergente da sigla oficial (silver.municipios.sigla_uf) invalida a linha."
    ),
    "ano": "Ano de referência da estimativa (int). Domínio: 2001 a 2025. Fora do intervalo/nulo é descartado.",
    "populacao": (
        "População residente estimada (long, > 0). Derivado de bronze.valor "
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
        "Dimensão degenerada: ano de referência da estimativa (int). "
        "Grão da fato: 1 linha por município x ano (2001-2025)."
    ),
    "populacao": (
        "Medida: população residente estimada (long). Vem de silver.populacao_estimada."
    ),
}
