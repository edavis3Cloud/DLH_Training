# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM delta.`/databricks-datasets/nyctaxi-with-zipcodes/subsampled`

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/nyctaxi-with-zipcodes/subsampled")
display(files)
