import re
import unicodedata

from pyspark.sql import DataFrame
from pyspark.sql import Column
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType

# Regex de validação por formato de data aceito em para_data_segura
# (com faixas válidas de mês 01-12 e dia 01-31)
PADRAO_DATA = {
    "yyyy-MM-dd": r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$",
}


def nulo_se_vazio(coluna: Column) -> Column:
    """
    Trim e normalização de representações textuais de vazio: '', 'null'
    (qualquer caixa) viram null de verdade — comum em arquivos gov.br.
    """
    texto = F.trim(coluna.cast("string"))

    return F.when(
        texto.isNull() | (texto == "") | (F.upper(texto) == "NULL"),
        None,
    ).otherwise(texto)


def mapear_valores(coluna, mapa: dict[str, str]) -> Column:
    """
    Substitui valores da coluna conforme dicionário {de: para} (when encadeado);
    sem correspondência resulta em null. Aceita nome da coluna (str) ou Column.
    """
    alvo = F.col(coluna) if isinstance(coluna, str) else coluna

    expr = None
    for de, para in mapa.items():
        cond = alvo.eqNullSafe(F.lit(de))
        expr = F.when(cond, F.lit(para)) if expr is None else expr.when(cond, F.lit(para))

    return expr


def para_double_seguro(coluna: Column) -> Column:
    """
    Converte para double de forma tolerante: só converte textos numéricos
    (aceitando vírgula decimal); qualquer outro valor vira null.

    Evita erro [CAST_INVALID_INPUT] quando o cluster roda com ANSI mode
    habilitado (padrão no Databricks).
    """
    texto = F.trim(coluna.cast("string"))

    return F.when(
        texto.rlike(r"^[+-]?([0-9]+([.,][0-9]*)?|[.,][0-9]+)$"),
        F.translate(texto, ",", ".").cast("double"),
    )


def para_data_segura(coluna: Column, formato: str = "yyyy-MM-dd") -> Column:
    """
    Converte para date de forma tolerante: só converte textos que casam
    com o formato esperado; qualquer outro valor vira null.

    Evita erro de parse quando o cluster roda com ANSI mode habilitado.
    """
    if formato not in PADRAO_DATA:
        raise ValueError(f"Formato de data sem padrão de validação definido: {formato}")

    texto = F.trim(coluna.cast("string"))

    return F.when(
        texto.rlike(PADRAO_DATA[formato]),
        F.to_date(texto, formato),
    )


def read_csv(
    spark,
    file_path: str,
    delimiter: str = ",",
    encoding: str = "Windows-1252",
    header: bool = True,
    infer_schema: bool = True,
) -> DataFrame:
    """
    Lê um CSV com encoding configurável. Para arquivos com linhas de título
    antes do cabeçalho (ex.: exportações SIDRA/IBGE), use header=False +
    infer_schema=False e descarte as linhas de controle no notebook.
    """
    return (
        spark.read
        .option("header", header)
        .option("inferSchema", infer_schema)
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

def read_ods(
    spark: SparkSession,
    file_path: str,
    sheet_name: int | str = 0,
    header: int = 0,
) -> DataFrame:
    """
    Lê um arquivo .ods (OpenDocument Spreadsheet) e retorna um Spark DataFrame
    com todas as colunas como string limpa.

    Requer o pacote `odfpy` instalado no cluster (%pip install odfpy).

    Parâmetros:
        spark: sessão Spark (injetada).
        file_path: caminho do arquivo (ex.: /Volumes/workspace/raw/IBGE/arquivo.ods).
        sheet_name: índice (0-based) ou nome da aba a ser lida.
        header: índice 0-based da linha de cabeçalho.
            Ex.: cabeçalho na linha 7 do relatório -> header=6.

    Comportamento:
        - Remove colunas/linhas totalmente vazias (comuns em relatórios com margens).
        - Converte cada célula para texto sem artefatos numéricos:
          códigos IBGE lidos como número viram string inteira (1100015.0 -> "1100015"),
          preservando códigos que perderiam zero à esquerda ou ganhariam ".0".
        - Células vazias/NaN viram null.
    """
    import math

    import pandas as pd

    pdf = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        header=header,
        engine="odf",
    )

    pdf = pdf.loc[:, ~pdf.columns.astype(str).str.startswith("Unnamed")]
    pdf = pdf.dropna(how="all")

    def celula_para_texto(valor):
        if valor is None:
            return None
        if isinstance(valor, float) and math.isnan(valor):
            return None
        if isinstance(valor, float) and valor.is_integer():
            return str(int(valor))
        texto = str(valor).strip()
        return texto if texto else None

    pdf = pdf.apply(lambda coluna: coluna.map(celula_para_texto))

    schema = StructType(
        [StructField(coluna, StringType(), True) for coluna in pdf.columns]
    )

    return spark.createDataFrame(pdf, schema)


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


def add_table_comment(spark, table_name: str, comment: str) -> None:
    escaped_comment = comment.replace("'", "''")

    spark.sql(
        f"""
        COMMENT ON TABLE {table_name}
        IS '{escaped_comment}'
        """
    )
