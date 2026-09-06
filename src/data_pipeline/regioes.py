from pyspark.sql import DataFrame
from pyspark.sql import functions as F


REGIOES = {
    "Norte": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
    "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "Centro-Oeste": ["DF", "GO", "MT", "MS"],
    "Sudeste": ["ES", "MG", "RJ", "SP"],
    "Sul": ["PR", "RS", "SC"],
}


def adicionar_regiao(df: DataFrame, coluna_sigla_uf: str = "sigla_uf") -> DataFrame:
    """
    Adiciona a coluna `regiao` (Norte, Nordeste, Centro-Oeste, Sudeste, Sul)
    a partir da sigla da UF (mapa oficial IBGE). UFs sem mapeamento ficam null.
    """
    condicao = None
    for regiao, ufs in REGIOES.items():
        expressao = F.col(coluna_sigla_uf).isin(*ufs)
        condicao = (
            F.when(expressao, F.lit(regiao))
            if condicao is None
            else condicao.when(expressao, F.lit(regiao))
        )

    return df.withColumn("regiao", condicao)