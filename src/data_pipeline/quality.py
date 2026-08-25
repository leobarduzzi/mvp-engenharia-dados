from pyspark.sql import Column
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


def resumo_invalidos(
    spark: SparkSession,
    df: DataFrame,
    regras: dict[str, Column],
) -> DataFrame:
    """
    Gera relatório de qualidade: para cada regra (expressão onde True = inválido),
    retorna a quantidade de registros inválidos e o percentual sobre o total.

    Parâmetros:
        spark: sessão Spark (injetada).
        df: DataFrame a ser avaliado (antes dos filtros).
        regras: dicionário {nome_da_regra: expressão booleana de invalidade}.

    Retorno:
        DataFrame com colunas [regra, qtd_invalidos, pct_sobre_total],
        pronto para display()/screenshot.
    """
    total = df.count()

    linhas = []
    for nome, condicao in regras.items():
        invalidos = df.filter(condicao).count()
        pct = round(100 * invalidos / total, 2) if total else 0.0
        linhas.append((nome, invalidos, pct))

    schema = StructType(
        [
            StructField("regra", StringType(), False),
            StructField("qtd_invalidos", IntegerType(), False),
            StructField("pct_sobre_total", DoubleType(), False),
        ]
    )

    return spark.createDataFrame(linhas, schema)


def condicao_valida(regras: dict[str, Column]) -> Column:
    """
    Combina as regras de invalidade em uma única expressão de validade
    (True = registro aprovado em todas as regras).
    """
    condicao = ~regras[next(iter(regras))]
    for cond in list(regras.values())[1:]:
        condicao = condicao & ~cond

    return condicao
