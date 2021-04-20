import numpy as np
import xlsxwriter as xl
import time

# Função utilizada: f(x) = 3 * cos(x) - e^x/3 // Intervalo: [-5; 2]// h: 0.75 // Precisão: 10^-5
# f'(x) = -3sen(x) - 1/3 * e^x


tempo_inicial = time.time()

# Utilizando o método de Newton para o intervalo [-5; -4.25]:

# Xo é um chute inicial de qualquer valor entre o intervalo I.


def test(x):
    resultado = 3 * np.cos(x) - (np.exp(x)/3)
    return resultado


def derivada(x):
    resultado = - 3 * np.sin(x) - (1/3) * (np.exp(x)/3)
    return resultado

def newton():
    c = 0
    x_barra = [-4.625]  # O Xo é um chute inicial de qualquer valor no I. Nesse caso, o valor do meio
    x_aplicado = []
    while True:
        x_aplicado_atual = test(x_barra[-1])
        if x_aplicado_atual < 0:
            modulo_x_aplicado_atual = x_aplicado_atual * (-1)
        else:
            modulo_x_aplicado_atual = x_aplicado_atual
        if modulo_x_aplicado_atual < 10 ** -5:
            x_aplicado.append(x_aplicado_atual)
            break
        else:
            derivada_x_barra = derivada(x_barra[-1])
            x_aplicado.append(x_aplicado_atual)
            x_barra_atual = x_barra[-1] - (x_aplicado[-1] / derivada_x_barra)
            x_barra.append(x_barra_atual)
            c += 1
    return x_barra[-1], x_barra, x_aplicado, c


raiz_aproximada = newton()[0]
lista_x_barra = newton()[1]
lista_x_aplicado = newton()[2]
iteracoes = newton()[3]

print('Questao teste, intervalo [-5; -4.25]:')
print(f'A raiz aproximada é: {raiz_aproximada}')
print(f'Para encontrar essa raiz, foram necessárias {iteracoes} iterações.')
print(lista_x_barra)
print(lista_x_aplicado)

"""# Criando a tabela com os valores obtidos
# Criando o arquivo
outWorkbook = xl.Workbook("Questao_03_1o_intervalo_newton.xlsx")
outSheet = outWorkbook.add_worksheet()

# Declarando os títulos

# Escrevendo os dados no arquivo
outSheet.write("A1", "x_barra")
outSheet.write("B1", "f(x_barra)")

for number, item in enumerate(lista_x_barra):
    outSheet.write(number + 1, 0, item)
for number, item in enumerate(lista_x_aplicado):
    outSheet.write(number + 1, 1, item)
outWorkbook.close()"""

tempo_final = time.time()
tempo_gasto = tempo_final - tempo_inicial
print(f'Foram gastos {tempo_gasto}s.')
