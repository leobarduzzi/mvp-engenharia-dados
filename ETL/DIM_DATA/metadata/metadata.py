# Catálogo de dados DIM_DATA - Dimensão de data (calendário completo)
#
# Fonte: NENHUMA fonte externa — calendário gerado proceduralmente.
# Linhagem: geração determinística em memória (sequence de datas diárias) ->
#            gold.dim_data
#
# A dimensão é conformada e reusada por todas as fatos via role-playing
# (ex.: fato_obras.sk_data_inicio e fato_obras.sk_data_situacao).
# As chaves dos dicionários são os nomes de colunas após a geração.

DIM_DATA_COMMENTS = {
    "sk_data": (
        "Surrogate Key da dimensão: inteiro no formato AAAAMMDD (ex.: 20250815). "
        "PK. Determinística (derivada da própria data, estável entre execuções)."
    ),
    "data": "Data do calendário (date). Grão da dimensão: 1 linha por dia.",
    "ano": "Ano da data (int). Domínio: 1990 a 2030.",
    "semestre": "Semestre do ano (int). Domínio: 1 a 2.",
    "trimestre": "Trimestre do ano (int). Domínio: 1 a 4.",
    "bimestre": "Bimestre do ano (int). Domínio: 1 a 6.",
    "mes": "Mês da data (int). Domínio: 1 a 12.",
    "nome_mes": (
        "Nome do mês em português (Janeiro a Dezembro). Derivado de mes."
    ),
    "dia": "Dia do mês (int). Domínio: 1 a 31.",
    "dia_semana": (
        "Número do dia na semana (int). Convenção: 1=Domingo a 7=Sábado. "
        "Derivado da função dayofweek."
    ),
    "nome_dia_semana": (
        "Nome do dia da semana em português (Domingo a Sábado). Derivado de dia_semana."
    ),
    "semana_do_ano": (
        "Semana do ano ISO (int). Domínio: 1 a 53. Derivado da função weekofyear."
    ),
    "ano_mes": (
        "Ano-mês no formato 'AAAA-MM' (string) para agregações mensais."
    ),
    "flag_fim_de_semana": (
        "Booleano: true quando o dia é sábado ou domingo (útil para análises de sazonalidade)."
    ),
}
