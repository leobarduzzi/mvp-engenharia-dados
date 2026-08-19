import re
import unicodedata

from pyspark.sql import DataFrame


def read_csv(
    spark,
    file_path: str,
    delimiter: str = ",",
    encoding: str = "Windows-1252"
) -> DataFrame:
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("delimiter", delimiter)
        .option("encoding", encoding)
        .csv(file_path)
    )


def save_table(
    df: DataFrame,
    table_name: str,
    mode: str = "overwrite"
) -> None:
    (
        df.write
        .format("delta")
        .mode(mode)
        .saveAsTable(table_name)
    )


def normalizar_texto(nome: str) -> str:
    nome = unicodedata.normalize("NFKD", nome)

    nome = "".join(
        c for c in nome
        if not unicodedata.combining(c)
    )

    nome = nome.lower()

    # Substitui qualquer sequência que não seja letra ou número por "_"
    nome = re.sub(r"[^a-z0-9]+", "_", nome)

    # Remove "_" duplicados
    nome = re.sub(r"_+", "_", nome)

    return nome.strip("_")


def normalizar_colunas(df: DataFrame) -> DataFrame:
    nomes = [
        normalizar_texto(col)
        for col in df.columns
    ]

    if len(nomes) != len(set(nomes)):
        duplicadas = [
            nome
            for nome in set(nomes)
            if nomes.count(nome) > 1
        ]

        raise ValueError(
            f"Colunas duplicadas após normalização: {duplicadas}"
        )

    return df.toDF(*nomes)

def add_column_comments(spark, table_name: str, comments: dict[str, str]) -> None:
    for column_name, comment in comments.items():
        escaped_comment = comment.replace("'", "''")

        spark.sql(
            f"""
            ALTER TABLE {table_name}
            ALTER COLUMN {column_name}
            COMMENT '{escaped_comment}'
            """
        )
