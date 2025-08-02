""" Verifica temperatura
try:
    temperatura_celsius = float(input("Informe a temperatura: "))
    fahrenheit = (temperatura_celsius * 9/5) + 32
    print(f"{temperatura_celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")"""

""" Verifica um palindromo
Frase = input("Insira uma frase/palavra: ")
if isinstance(Frase,str):
    formate = Frase.replace(" ", "").lower()
    if formate == formate[::-1]:
        print("É um palindromo.")
    else:
        print("Não é um palindromo.")
else:
    print("Entrada inválida. Digite uma palavra ou frase.")"""

"""Calculadora simples
try:
    Valor_um = float(input("Insira um número: "))
    Valor_dois = float(input("Insira um número: "))
    Operador = input("Informa o operador = ")
    if Operador == '+':
        resultado = Valor_um + Valor_dois
    elif Operador == '-':
        resultado = Valor_um - Valor_dois
    elif Operador == '*':
        resultado = Valor_um * Valor_dois
    elif Operador == '/':
        resultado = Valor_um/Valor_dois
    else:
        print("Operador invalido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Deve ser inserido números")"""

"""Classificador de números
try:
    Numero = float(input('Insira um número: '))
    if Numero < 0:
        print("O número é negativo")
    elif Numero > 0:
        print("O numero é positivo")
    else:
        print("O numero é igual a 0")
    if Numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
except ValueError:
    print("Deve ser informado um número.")"""

#Lista de números
entrada_numero = input("Informe uma lista de números(separado por virgula): ")
numero_string = entrada_numero.split(",")
numero_int = []
try:
    for num in numero_string:
        numero_int.append(int(num.strip()))
        print("A lista de inteiros é", numero_int)
except ValueError:
    print("Erro: Certifique-se que todos os elementos são números inteiros.")




