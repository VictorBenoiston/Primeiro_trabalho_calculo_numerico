import xlsxwriter as xl
import time
import numpy as np

# Chute inicial entre o intervalo // Intervalo = [-2; -1.5] // f(x) = cos(x) + e^x // função de iteração = ln(-cos(x))
# Precisão = 10^-7


def test(x):
    resultado = np.cos(x) + np.exp(x)
    return resultado


def funcao_iteracao(x):
    resultado = np.log(-(np.cos(x)))
    return resultado


def ponto_fixo():
    c = 0
    x_barra = [-1.75]
    x_aplicado = []    # Adotei como x0 o valor de -1.75 (Meio do intervalo)
    while True:
        x_aplicado_atual = test(x_barra[-1])
        if x_aplicado_atual < 0:
            modulo_x_aplicado_atual = x_aplicado_atual * (-1)
        else:
            modulo_x_aplicado_atual = x_aplicado_atual
        if modulo_x_aplicado_atual < 10 ** -7:
            x_aplicado.append(x_aplicado_atual)
            break
        else:
            x_barra_atual = funcao_iteracao(x_barra[-1])
            x_barra.append(x_barra_atual)
            x_aplicado.append(x_aplicado_atual)
            c += 1
    return x_barra[-1], x_barra, x_aplicado, c


raiz_aproximada = ponto_fixo()[0]
lista_x_barra = ponto_fixo()[1]
lista_x_aplicado = ponto_fixo()[2]
iteracoes = ponto_fixo()[3]

print('Questao teste, intervalo [-2; -1.5]:')
print(f'A raiz aproximada é: {raiz_aproximada}')
print(f'Para encontrar essa raiz, foram necessárias {iteracoes} iterações.')
print(lista_x_barra)
print(lista_x_aplicado)

# Conclusão: A função de iteração fi(x) = ln(-cos(x)) não é contínua em todos os pontos do intervalo.

# --------

# Chute inicial entre o intervalo // Intervalo = [-2; -1.5] // f(x) = cos(x) + e^x // função de iteração = ln(-cos(x))
# Precisão = 10^-7

# def test(x):
#     resultado = np.cos(x) + np.exp(x)
#     return resultado
#
#
# def funcao_iteracao(x):
#     resultado = np.arccos(-np.exp(x))
#     return resultado


# def ponto_fixo():
#     c = 0
#     x_barra = [-1.75]
#     x_aplicado = []    # Adotei como x0 o valor de -1.75 (Meio do intervalo)
#     while True:
#         x_aplicado_atual = test(x_barra[-1])
#         if x_aplicado_atual < 0:
#             modulo_x_aplicado_atual = x_aplicado_atual * (-1)
#         else:
#             modulo_x_aplicado_atual = x_aplicado_atual
#         if modulo_x_aplicado_atual < 10 ** -7:
#             x_aplicado.append(x_aplicado_atual)
#             break
#         else:
#             x_barra_atual = funcao_iteracao(x_barra[-1])
#             x_barra.append(x_barra_atual)
#             x_aplicado.append(x_aplicado_atual)
#             c += 1
#     return x_barra[-1], x_barra, x_aplicado, c
#
#
# raiz_aproximada = ponto_fixo()[0]
# lista_x_barra = ponto_fixo()[1]
# lista_x_aplicado = ponto_fixo()[2]
# iteracoes = ponto_fixo()[3]
#
# print('Questao teste, intervalo [-5; -4.5]:')
# print(f'A raiz aproximada é: {raiz_aproximada}')
# print(f'Para encontrar essa raiz, foram necessárias {iteracoes} iterações.')
# print(lista_x_barra)
# print(lista_x_aplicado)

# Conclusão: Embora satisfaça todos os três requisistos de convergência, ao aplicar o
# x_barra na função de iteração, o valor obtido não pertence ao intervalo [-2; -1.5]
