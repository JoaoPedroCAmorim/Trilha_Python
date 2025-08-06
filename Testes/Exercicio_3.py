# IF:
"""try:
    QNTD: float = float(input("Informe a quantidade de vendas: "))
    Preco: float = float(input("Informe o preço da venda: "))
    if QNTD > 0 and Preco > 0:
        print("Dados válidos")
    else:
        print("Dados inválidos")
except ValueError:
    print("Erro: Entrada inválida. Deve ser inserido números")
    exit()
Valor_venda: float = QNTD * Preco
print("O valor vendido é", Valor_venda)"""

"""try:
    temperatura: float = float(input("Informe a temperatura atual: "))
    if temperatura < 18:
        print("A temperatura atual está baixa")
    elif 18<= temperatura <= 26:
        print("A temperatura atual é normal")
    else:
        print("A temperatura é atual está alta")
except ValueError:
    print("Erro: Entrada inválida. Deve ser inserido números")
    exit()"""

"""log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])"""

"""idade: int = int(input("Informe a sua idade: "))
email: str = input("Informe seu e-mail: ")
if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email:
    print("Email inválido")
else:
    print("Dados de usuário válidos")"""
# FOR
"""texto = input("Por favor, informe a palavra chave: ")
palavras = texto.split()
contagem_palavras = {}
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
    print(contagem_palavras)"""

"""numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
print(normalizados)"""

"""usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]
usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]
print(usuarios_validos)"""

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor
print(total_por_categoria)