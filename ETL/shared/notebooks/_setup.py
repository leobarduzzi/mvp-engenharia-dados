# Databricks notebook source
# DBTITLE 1,Configuração do ambiente
# Setup do ambiente mvp-engenharia-dados
# Use este notebook via %run no início de outros notebooks

import sys

# Adiciona o pacote data_pipeline ao path
if "/Workspace/mvp-engenharia-dados/src" not in sys.path:
    sys.path.insert(0, "/Workspace/mvp-engenharia-dados/src")

print("✓ Setup concluído: data_pipeline disponível")

# COMMAND ----------

