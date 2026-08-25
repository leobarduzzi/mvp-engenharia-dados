# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Setup DTB
# MAGIC %run ../../shared/notebooks/_setup

# COMMAND ----------

# DBTITLE 1,Instala dependência ODS (odfpy)
# MAGIC %pip install odfpy --quiet

# COMMAND ----------

# DBTITLE 1,Instala dependência conversão IBGE<->TOM (cidade-ibge-tom)
# MAGIC %pip install git+https://github.com/leogregianin/cidade_ibge_tom.git --quiet
# MAGIC
# MAGIC # Obs.: o wheel publicado no PyPI (0.1.1) está quebrado — o arquivo
# MAGIC # __init__.py sai como "__init__py" e a importação falha. Instalamos da
# MAGIC # fonte oficial no GitHub, onde o pacote está correto.

# COMMAND ----------

# DBTITLE 1,Adiciona metadata DTB
import sys

if "/Workspace/mvp-engenharia-dados/ETL/DTB" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/ETL/DTB")
