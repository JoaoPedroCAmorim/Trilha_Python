import pandas as pd
import os
import glob

# Função para ler e consolidar o JSON https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
pasta = 'dados'
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) #lendo os arquivos
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] # listando e tranformandos os arquivos em dataframe
    df_total = pd.concat(df_list, ignore_index=True) #concatenando os arquivos
    return df_total

# Transforma
def calcular_kpi_total_vendas(df:pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Função que carrega um CSV ou Parquet
def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("data.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)


def pipeline_calcular_kpi_consolidado(pasta: str, formato_de_saida: list):   
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_calculado,formato_de_saida)