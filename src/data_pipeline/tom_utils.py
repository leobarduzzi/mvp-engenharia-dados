from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


def enriquecer_codigo_tom(
    spark: SparkSession,
    df: DataFrame,
    coluna_codigo_ibge: str = "codigo_municipio",
    coluna_codigo_tom: str = "codigo_tom",
) -> DataFrame:
    """
    Enriquece o DataFrame com o código TOM (4 dígitos, padrão SIAFI/Tesouro)
    correspondente ao código IBGE do município (7 dígitos com DV).

    Usa a biblioteca `cidade-ibge-tom` (MIT), cuja base deriva da lista oficial
    de municípios do SIAFI (Tesouro Transparente). A conversão é feita no driver
    (tabela estática ~5.5k municípios) e distribuída via left join — códigos sem
    correspondência recebem null.

    Parâmetros:
        spark: sessão Spark (injetada).
        df: DataFrame contendo a coluna com o código IBGE.
        coluna_codigo_ibge: nome da coluna com o código IBGE (join key).
        coluna_codigo_tom: nome da coluna de saída com o código TOM.
    """
    from cidade_ibge_tom import info_cidade

    codigos = sorted({row[0] for row in df.select(coluna_codigo_ibge).distinct().collect()})

    linhas = []
    for codigo in codigos:
        info = info_cidade(codigo=codigo)
        tom = info.get("tom") if info else None
        linhas.append((codigo, tom))

    schema = StructType(
        [
            StructField(coluna_codigo_ibge, StringType(), True),
            StructField(coluna_codigo_tom, StringType(), True),
        ]
    )
    mapping = spark.createDataFrame(linhas, schema)

    return df.join(mapping, on=coluna_codigo_ibge, how="left")
