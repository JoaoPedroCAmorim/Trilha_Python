import csv
path_arquivo = "vendas_2.csv"

# função para ler o arquivo csv
def leitor_csv(caminho:str):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

# Função para processar os dados
def processar_dados (dados):
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

# Função para calcular as vendas por categoria
def calcular_vendas_categoria(dados):
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

# Função principal
def main():
    dados_brutos = leitor_csv(path_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categorias = calcular_vendas_categoria(dados_processados)
    for categoria, total in vendas_categorias.items():
        print(f'{categoria}: ${total}')
if __name__== '__main__':
    main()