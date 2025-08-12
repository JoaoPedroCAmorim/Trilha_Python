Valor_1 = 4
Valor_2 = 6
Valor_3 = Valor_1 + Valor_2

Valor_4 = 6
Valor_5 = 4
Valor_6 = Valor_4 + Valor_5

def soma(Valor_1_soma: float, Valor_2_soma: float) -> float:
    """uma funçao simples de soma"""
    Resultado_soma = Valor_1_soma + Valor_2_soma
    return Resultado_soma

valor_3 = soma(Valor_1_soma= Valor_1, Valor_2_soma= Valor_2)
valor_6 = soma(Valor_4, Valor_5)

print(Valor_3)
print(valor_6)