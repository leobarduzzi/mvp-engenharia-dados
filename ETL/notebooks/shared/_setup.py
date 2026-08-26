# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Setup global do projeto (mvp-engenharia-dados)
# Setup único: usado via `%run ../shared/_setup` no início de qualquer notebook.
# Expõe `src` (data_pipeline) e `ETL` (pacote catalogo) no sys.path e recarrega
# os módulos do projeto já importados — permite iterar nos .py sem reiniciar o cluster.

# COMMAND ----------

# DBTITLE 1,Instala dependências de terceiros (idempotente)
# MAGIC %pip install odfpy --quiet
# MAGIC
# MAGIC # cidade-ibge-tom: o wheel do PyPI (0.1.1) está quebrado (__init__.py sai como
# MAGIC # "__init__py" e a importação falha). Instalamos da fonte oficial no GitHub.
# MAGIC %pip install git+https://github.com/leogregianin/cidade_ibge_tom.git --quiet

# COMMAND ----------

# DBTITLE 1,Path + reload de data_pipeline/catalogo
import sys

# Remove do cache módulos já carregados do projeto, para recarregar a versão atual
for _modulo in [
    m for m in list(sys.modules)
    if m.startswith("data_pipeline") or m.startswith("catalogo")
]:
    del sys.modules[_modulo]

# Expõe os pacotes do projeto
for _path in (
    "/Workspace/mvp-engenharia-dados/src",
    "/Workspace/mvp-engenharia-dados/ETL",
):
    if _path not in sys.path:
        sys.path.insert(0, _path)

print("✓ Setup concluído: data_pipeline e catalogo disponíveis")