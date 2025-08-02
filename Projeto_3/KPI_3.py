constante_bonus = 1000
nome_valido = False
salario_valido = False
bonus_valido = False
# Usuário deve inserir o nome
while nome_valido is not True:
    try:
        nome_usuario = input("Digite seu nome: ")
    #verifica se contem apenas numeros
        if any(char.isdigit()for char in nome_usuario):
            raise ValueError("O nome não pode conter números!")
    # verifica se o campo esta em branco
        elif len(nome_usuario) == 0:
            raise ValueError("O campo esta em branco.")
    # verifica se há somente espaço
        elif nome_usuario.isspace():
            raise ValueError("Foi informado somente espaço.")
        else:
            nome_valido = True
            print("Nome válido:", nome_usuario)
    except ValueError as Erro:
        print(Erro)
# Usuário deve informar o salário - Float converte a entrada (input) para um numero com ponto
while salario_valido is not True:
    try:
        salario_usuario = float(input("Informe seu salário: "))
        if salario_usuario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
            ("Por favor, informar um valor válido!")
# Usuário deve informar o bonus
while bonus_valido is not True:
    try:
        bonus_usuario = float(input("Informe seu bonus: "))
        if bonus_usuario < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
# Calculo do bonus final
valor_bonus = constante_bonus + salario_usuario * bonus_usuario

'''Imprima a mensagem personalizada contendo o nome do usuário e o valor do bonus,
para imprimir variaveis e texto utilizar o print(f)'''
print(f"O usuário {nome_usuario} possui o bonus de R$ {valor_bonus}")
