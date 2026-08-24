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

# DBTITLE 1,Adiciona metadata DTB
import sys

if "/Workspace/mvp-engenharia-dados/ETL/DTB" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/ETL/DTB")
