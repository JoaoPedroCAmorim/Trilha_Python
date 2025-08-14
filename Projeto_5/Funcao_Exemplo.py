Valor_1 = 4
Valor_2 = 6
Valor_3 = Valor_1 + Valor_2

Valor_4 = 6
Valor_5 = 4
Valor_6 = Valor_4 + Valor_5

def soma(Valor_1_soma: float, Valor_2_soma: float) -> float:
    # uma funçao simples de soma
    Resultado_soma = Valor_1_soma + Valor_2_soma
    return Resultado_soma

valor_3 = soma(Valor_1_soma= Valor_1, Valor_2_soma= Valor_2)
valor_6 = soma(Valor_4, Valor_5)

print(Valor_3)
print(valor_6)

# Calculo da Média de Valores em uma Lista
from typing import List
def calcular_media(valores: List[float]) -> float:
    return sum(valores)/len(valores)
#media_valores = calcular_media([1,2,3,4,5,6])
#print(media_valores)

# Filtrar dados acima de um limite
valores = [1, 2, 3, 4, 5, 6]
limite=3
def filtrar_valores(valores: List[float], limite:float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado
#valores_acima_limite = filtrar_valores(valores,limite)
#print(valores_acima_limite)

# Contagem de valores unicos de uma lista
lista = [5,5,6,6,7,8,10,12,13,14,15,15]
def valores_unicos(lista: list[int]) -> int:
    return len(set(lista))
#contagem_valores = valores_unicos(lista)
#print(contagem_valores)

# Desvio Padrão
lista_valores = [5,7,8,2,3]
def calcular_desvio_padrao(lista_valores: list[int]) -> int:
    media = sum(lista_valores)/len(lista_valores)
    variancia = sum((x - media)** 2 for x in lista_valores)/ len(lista_valores)
    return variancia ** 0.5
desvio_padrao = calcular_desvio_padrao(lista_valores)
print(desvio_padrao)