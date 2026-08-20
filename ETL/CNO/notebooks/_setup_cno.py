# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Setup CNO
# MAGIC %run ../../shared/notebooks/_setup

# COMMAND ----------

# DBTITLE 1,Adiciona metadata CNO
import sys

# Setup específico do pipeline CNO
# O setup compartilhado já configurou data_pipeline
# Aqui adicionamos apenas o módulo metadata específico do CNO

if "/Workspace/mvp-engenharia-dados/ETL/CNO" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/ETL/CNO")

print("✓ Setup CNO concluído (metadata CNO disponível)")