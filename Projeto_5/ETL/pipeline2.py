from etl import ler_csv, filtrar_produtos_nao_entregues

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)