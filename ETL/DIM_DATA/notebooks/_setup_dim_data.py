# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Setup DIM_DATA
# MAGIC %run ../../shared/notebooks/_setup

# COMMAND ----------

# DBTITLE 1,Adiciona metadata DIM_DATA
import sys

if "/Workspace/mvp-engenharia-dados/ETL/DIM_DATA" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/ETL/DIM_DATA")
