from etl_pandas import pipeline_calcular_kpi_consolidado

pasta: str = 'dados'
formato_de_saida = ["csv", "parquet"]

pipeline_calcular_kpi_consolidado(pasta,formato_de_saida)
