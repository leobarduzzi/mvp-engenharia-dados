# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Setup POP (Estimativa Populacional)
# MAGIC %run ../../shared/notebooks/_setup

# COMMAND ----------

# DBTITLE 1,Adiciona metadata POP
import sys

if "/Workspace/mvp-engenharia-dados/ETL/POP" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/ETL/POP")
