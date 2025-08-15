import csv
path_arquivo = "vendas.csv"

# funcao para transformar o CSV em lista de dicionario
def ler_csv(vendas: str) -> list[dict]:
    lista = []
    with open(vendas, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# funcao para filtrar os produtos entregues
def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    lista_com_produtos_filtrados = []
    for produtos in lista:
        if produtos.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produtos)
    return lista_com_produtos_filtrados

# funcao para somar valores da lista
def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    valor_total = 0
    for produtos in lista_com_produtos_filtrados:
        valor_total += int(produtos.get("preco"))
    return valor_total