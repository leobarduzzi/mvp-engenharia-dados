# Databricks notebook source
# MAGIC %pip install odfpy openpyxl pandas --quiet
# MAGIC dbutils.library.restartPython()
# COMMAND ----------

# DBTITLE 1,Setup DTB
# MAGIC %run ../../shared/notebooks/_setup

# COMMAND ----------

# DBTITLE 1,Adiciona metadata DTB
import sys

if "/Workspace/mvp-engenharia-dados/ETL/DTB" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/ETL/DTB")
