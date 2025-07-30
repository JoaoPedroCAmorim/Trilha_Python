constante_bonus = 1000
# Usuário deve inserir o nome
try:
    nome_usuario = input("Digite seu nome: ")
#verifica se contem apenas numeros
    if any(char.isdigit()for char in nome_usuario):
        raise ValueError("O nome não pode conter números!")
        exit()
# verifica se o campo esta em branco
    elif len(nome_usuario) == 0:
        raise ValueError("O campo esta em branco.")
        exit()
# verifica se há somente espaço
    elif nome_usuario.isspace():
        raise ValueError("Foi informado somente espaço.")
        exit()
    else:
        print("Nome válido:", nome_usuario)
except ValueError as Erro:
    print(Erro)
    exit()
# Usuário deve informar o salário e o bonus - Float converte a entrada (input) para um numero com ponto
try:
    salario_usuario = float(input("Informe seu salário: "))
    bonus_usuario = float(input("Informe seu bonus: "))
    if salario_usuario < 0:
        raise ValueError("Por favor, informar um valor válido!")
    elif bonus_usuario < 0:
        raise ValueError("Por favor, informar um valor válido!")
except ValueError as e:
    print(e)
    exit()
# Calculo do bonus final
valor_bonus = constante_bonus + salario_usuario * bonus_usuario

'''Imprima a mensagem personalizada contendo o nome do usuário e o valor do bonus,
para imprimir variaveis e texto utilizar o print(f)'''
print(f"O usuário {nome_usuario} possui o bonus de R$ {valor_bonus}")
