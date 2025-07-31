constante_bonus = 1000
# Usuário deve inserir o nome
nome_usuario = input("Digite seu nome: ")

# Usuário deve informar o salário - Float converte a entrada (input) para um numero de ponto
salario_usuario = float(input("Informe seu salário: "))

# Informe o seu bônus
bonus_usuario = float(input("Informe seu bonus: "))

# Calculo do bonus final
valor_bonus = constante_bonus + salario_usuario * bonus_usuario

'''Imprima a mensagem personalizada contendo o nome do usuário e o valor do bonus,
para imprimir variaveis e texto utilizar o print(f)'''
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus}")
