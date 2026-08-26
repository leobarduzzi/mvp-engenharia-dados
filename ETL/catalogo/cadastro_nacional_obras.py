CNO_COMMENTS = {
    "cno": "Número do CNO",
    "codigo_do_pais": "Código do país",
    "nome_do_pais": "Nome do País",
    "data_de_inicio": "Data de início da obra (AAAA-MM-DD)",
    "data_de_inicio_da_responsabilidade": "Data de início da responsabilidade da obra (AAAA-MM-DD)",
    "data_de_registro": "Data de registro (AAAA-MM-DD)",
    "cno_vinculado": "Número da inscrição vinculada da obra",
    "cep": "Número do CEP (somente Brasil)",
    "ni_do_responsavel": "NI do responsável pela obra (CPF: campo em branco)",
    "qualificacao_do_responsavel": (
        "Qualificação do responsável: "
        "0053-Construtora;" 
        "0057-Dono da Obra; "
        "0064-Incorporador;"
        "0070-Proprietário; "
        "0109-Consórcio;"
        "0110-Construção em nome coletivo; "
        "0111-Sociedade Líder de Consórcio"
    ),
    "nome": "Nome da obra",
    "codigo_do_municipio": "Código do município (TOM)",
    "nome_do_municipio": "Nome do município",
    "tipo_de_logradouro": "Tipo de logradouro",
    "logradouro": "Logradouro",
    "numero_do_logradouro": "Número do logradouro",
    "bairro": "Bairro",
    "estado": "Estado",
    "caixa_postal": "Caixa postal no exterior",
    "complemento": "Complemento do endereço",
    "unidade_de_medida": "Unidade de medida da obra",
    "area_total": "Valor da área total da obra",
    "situacao": (
        "Situação da obra: "
        "01-NULA; 02-ATIVA;"
        "03-SUSPENSA; "
        "14-PARALISADA;"
        "15-ENCERRADA"
    ),
    "data_da_situacao": "Data da situação da obra (AAAA-MM-DD)",
    "nome_empresarial": (
        "Nome empresarial do responsável "
        "(pessoa física: campo em branco)"
    ),
    "codigo_de_localizacao": "Código da localização",
}

CNO_AREA_COMMENTS = {
    "cno": "Número do CNO",
    "categoria": (
        "Categoria da área: "
        "0-Obra Nova; "
        "1-Acréscimo; "
        "2-Reforma; "
        "3-Demolição; "
        "4-Existente"
    ),
    "destinacao": (
        "Destinação da área: "
        "0-Residencial unifamiliar; "
        "1-Residencial multifamiliar; "
        "2-Comercial salas e lojas; "
        "3-Edifício de Garagens; "
        "4-Galpão industrial; "
        "5-Casa popular; "
        "6-Conjunto habitacional popular"
    ),
    "tipo_de_obra": (
        "Tipo de obra: "
        "0-Alvenaria; "
        "1-Madeira; "
        "2-Mista"
    ),
    "tipo_de_area": (
        "Tipo de área: "
        "P-Principal; "
        "C-Complementar"
    ),
    "tipo_de_area_complementar": (
        "Tipo de área complementar: "
        "0-Quadra Esportiva e Poliesportiva; "
        "1-Estacionamento Térreo; "
        "2-Piscina; "
        "3-Área Complementar do Posto de Gasolina"
    ),
    "metragem": "Metragem da área",
}

# ---------------------------------------------------------------------------
# Domínios oficiais (código -> descrição). Fonte: layout dados.gov.br / RFB.
# Usados para validação na silver e decodificação nas dimensões da gold.
# ---------------------------------------------------------------------------

DOMINIO_SITUACAO = {
    "01": "NULA",
    "02": "ATIVA",
    "03": "SUSPENSA",
    "14": "PARALISADA",
    "15": "ENCERRADA",
}

DOMINIO_CATEGORIA = {
    "0": "Obra Nova",
    "1": "Acréscimo",
    "2": "Reforma",
    "3": "Demolição",
    "4": "Existente",
}

DOMINIO_DESTINACAO = {
    "0": "Residencial unifamiliar",
    "1": "Residencial multifamiliar",
    "2": "Comercial salas e lojas",
    "3": "Edifício de Garagens",
    "4": "Galpão industrial",
    "5": "Casa popular",
    "6": "Conjunto habitacional popular",
}

DOMINIO_TIPO_DE_OBRA = {
    "0": "Alvenaria",
    "1": "Madeira",
    "2": "Mista",
}

DOMINIO_TIPO_DE_AREA = {
    "P": "Principal",
    "C": "Complementar",
}

DOMINIO_TIPO_DE_AREA_COMPLEMENTAR = {
    "0": "Quadra Esportiva e Poliesportiva",
    "1": "Estacionamento Térreo",
    "2": "Piscina",
    "3": "Área Complementar do Posto de Gasolina",
}

# ---------------------------------------------------------------------------
# Silver
# ---------------------------------------------------------------------------

SILVER_CNO_COMMENTS = {
    "cno": (
        "Número do CNO (inscrição da obra). PK natural. "
        "Vem de bronze.cno.cno (trim)."
    ),
    "data_de_inicio": (
        "Data de início da obra (date, formato AAAA-MM-DD). "
        "Derivado de bronze.cno.data_de_inicio; inválidos/nulos descartados."
    ),
    "codigo_do_municipio": (
        "Código TOM do município informado no CNO (padrão SIAFI, 4 dígitos com pad à esquerda). "
        "Normalizado para o formato canônico e validado contra silver.municipios.codigo_tom "
        "(enriquecimento via cidade-ibge-tom/SIAFI); registros sem correspondência são descartados."
    ),
    "unidade_de_medida": "Unidade de medida da área da obra. Vem de bronze.cno.unidade_de_medida (trim).",
    "area_total": (
        "Área total da obra (double, >= 0). Derivado de bronze.cno.area_total "
        "com cast numérico; nulos/negativos descartados."
    ),
    "situacao": (
        "Situação da obra (código): 01-NULA; 02-ATIVA; 03-SUSPENSA; "
        "14-PARALISADA; 15-ENCERRADA. Valores fora do domínio são descartados."
    ),
    "data_da_situacao": (
        "Data da situação da obra (date, AAAA-MM-DD). "
        "Derivado de bronze.cno.data_da_situacao; inválidos/nulos descartados."
    ),
}

SILVER_CNO_AREAS_COMMENTS = {
    "cno": "Número do CNO (inscrição da obra). FK para silver.cno.",
    "categoria": (
        "Categoria da área em TEXTO, conforme arquivo origem (o CSV traz a descrição, não o código). "
        "Domínio: 'Obra Nova'; 'Acréscimo'; 'Reforma'; 'Demolição'; 'Existente'. Fora do domínio é descartado."
    ),
    "destinacao": (
        "Destinação da área em TEXTO, conforme arquivo origem. "
        "Domínio: 'Residencial unifamiliar'; 'Residencial multifamiliar'; "
        "'Comercial salas e lojas'; 'Edifício de Garagens'; 'Galpão industrial'; "
        "'Casa popular'; 'Conjunto habitacional popular'. Fora do domínio é descartado."
    ),
    "tipo_de_obra": (
        "Tipo de obra em TEXTO, conforme arquivo origem. "
        "Domínio: 'Alvenaria'; 'Madeira'; 'Mista'. Fora do domínio é descartado."
    ),
    "tipo_de_area": (
        "Tipo de área em TEXTO, conforme arquivo origem. "
        "Domínio: 'Principal'; 'Complementar'. Fora do domínio é descartado."
    ),
    "tipo_de_area_complementar": (
        "Tipo de área complementar em TEXTO, conforme arquivo origem. "
        "Domínio: 'Quadra Esportiva e Poliesportiva'; 'Estacionamento Térreo'; 'Piscina'; "
        "'Área Complementar do Posto de Gasolina'. O literal 'null' do CSV é normalizado para null; "
        "pode ser nulo quando tipo_de_area = Principal (não aplicável); valor presente fora do domínio é descartado."
    ),
    "metragem": (
        "Metragem da área (double, >= 0). Derivado de bronze.cno_areas.metragem "
        "com conversão tolerante; nulos/negativos descartados."
    ),
}

# ---------------------------------------------------------------------------
# Gold
# ---------------------------------------------------------------------------

DIM_SITUACAO_COMMENTS = {
    "sk_situacao": "Surrogate Key da dimensão (int sequencial ordenada por codigo_situacao). PK.",
    "codigo_situacao": (
        "Código da situação da obra (NK): 01-NULA; 02-ATIVA; 03-SUSPENSA; "
        "14-PARALISADA; 15-ENCERRADA. Vem de silver.cno.situacao."
    ),
    "descricao": (
        "Descrição da situação decodificada via domínio oficial RFB "
        "(NULA, ATIVA, SUSPENSA, PARALISADA, ENCERRADA)."
    ),
}

DIM_AREA_COMMENTS = {
    "sk_area": (
        "Surrogate Key da dimensão (int sequencial, ordenada pelos atributos). PK. "
        "Grão: 1 linha por combinação categoria x destinação x tipo de obra x tipo de área x tipo complementar."
    ),
    "categoria": (
        "Descrição textual oficial da categoria: 'Obra Nova'; 'Acréscimo'; 'Reforma'; "
        "'Demolição'; 'Existente'. Vem de silver.cno_areas (o arquivo origem traz texto)."
    ),
    "categoria_codigo": "Código RFB da categoria derivado do texto via domínio oficial: 0-Obra Nova; 1-Acréscimo; 2-Reforma; 3-Demolição; 4-Existente.",
    "destinacao": (
        "Descrição textual oficial da destinação: 'Residencial unifamiliar'; 'Residencial multifamiliar'; "
        "'Comercial salas e lojas'; 'Edifício de Garagens'; 'Galpão industrial'; 'Casa popular'; "
        "'Conjunto habitacional popular'. Vem de silver.cno_areas."
    ),
    "destinacao_codigo": "Código RFB da destinação derivado do texto via domínio oficial (0 a 6).",
    "tipo_de_obra": "Descrição textual oficial do tipo de obra: 'Alvenaria'; 'Madeira'; 'Mista'. Vem de silver.cno_areas.",
    "tipo_de_obra_codigo": "Código RFB do tipo de obra derivado do texto via domínio oficial: 0-Alvenaria; 1-Madeira; 2-Mista.",
    "tipo_de_area": "Descrição textual oficial do tipo de área: 'Principal' ou 'Complementar'. Vem de silver.cno_areas.",
    "tipo_de_area_codigo": "Código RFB do tipo de área derivado do texto via domínio oficial: P-Principal; C-Complementar.",
    "tipo_de_area_complementar": (
        "Descrição textual oficial do tipo complementar ('Quadra Esportiva e Poliesportiva'; "
        "'Estacionamento Térreo'; 'Piscina'; 'Área Complementar do Posto de Gasolina'); "
        "nulo quando não aplicável (tipo_de_area = Principal)."
    ),
    "tipo_de_area_complementar_codigo": "Código RFB do tipo complementar derivado do texto via domínio oficial (0 a 3); nulo quando não aplicável.",
}

FATO_OBRAS_COMMENTS = {
    "cno": (
        "Número do CNO (inscrição da obra). NK da obra. A fatos repete a obra "
        "por área declarada (grão: 1 linha por obra x área). Vem de silver.cno."
    ),
    "sk_data_inicio": (
        "SK role-playing de gold.dim_data para data_de_inicio (int AAAAMMDD, determinística)."
    ),
    "data_de_inicio": (
        "Data de início da obra (date). Apenas obras iniciadas a partir de 1990-01-01. Vem de silver.cno."
    ),
    "sk_data_situacao": (
        "SK role-playing de gold.dim_data para data_da_situacao (int AAAAMMDD, determinística)."
    ),
    "data_da_situacao": "Data da situação da obra (date). Vem de silver.cno.",
    "sk_situacao": "FK para gold.dim_situacao (situação da obra). Derivado de silver.cno.situacao.",
    "sk_municipio": (
        "FK para gold.dim_municipio (localização da obra). Join por código TOM: "
        "silver.cno.codigo_do_municipio (pad 4 dígitos) = gold.dim_municipio.codigo_tom."
    ),
    "sk_area": (
        "FK para gold.dim_area (perfil da área declarada). Derivado das colunas de silver.cno_areas."
    ),
    "unidade_de_medida": (
        "Unidade de medida da área (dimensão degenerada, texto original do CNO). Vem de silver.cno."
    ),
    "area_total": (
        "Medida: área total da obra (double). Repetida por linha de área. Vem de silver.cno."
    ),
    "metragem": (
        "Medida: metragem da área declarada (double), no grão obra x área. Vem de silver.cno_areas."
    ),
}
