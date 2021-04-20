import xlsxwriter as xl
import time
import numpy as np

# Função utilizada: f(x) = 3x^4-x²+x-5 // Intervalo: [-2; 2]// h: 0.25 // Precisão: 10^-4

tempo_inicial = time.time()

# Utilizando o método da falsa posição para o intervalo [1; 1.25]:


def test(x):
    x_barra_aplicado = (3*x**4 - x ** 2 + x - 5)
    return x_barra_aplicado


def falsa_posicao():
    c = 0
    valores_a = [1]  # Valores positivos
    valores_b = [1.25]  # Valores negativos
    a_aplicado = []
    b_aplicado =[]
    x_barra_aplicados = []
    x_barra = []
    while True:
        a_aplicado_atualizado = test(valores_a[-1])
        a_aplicado.append(a_aplicado_atualizado)
        b_aplicado_atualizado = test(valores_b[-1])
        b_aplicado.append(b_aplicado_atualizado)
        x_barra_atualizado = (valores_a[-1] * b_aplicado[-1] - valores_b[-1] * a_aplicado[-1]) / (b_aplicado[-1] - a_aplicado[-1])
        x_barra.append(x_barra_atualizado)      # Acima, temos a fórmula para a atualização da raiz aproximada
        validacao = test(x_barra[-1])
        if validacao < 0:
            modulo_validacao = validacao * (-1)
            valores_b.append(x_barra_atualizado)
            valores_a.append(valores_a[-1])
        else:
            modulo_validacao = validacao
            valores_a.append(x_barra_atualizado)
            valores_b.append(valores_b[-1])
        if modulo_validacao < 10 ** -4:
            x_barra_aplicados.append(validacao)
            break
        else:
            x_barra_aplicados.append(validacao)
            c += 1
    raiz_aproximada = f'{x_barra[-1]:.5f}'
    return raiz_aproximada, c, x_barra, x_barra_aplicados, valores_a, valores_b, a_aplicado, b_aplicado


raiz_aproximada = falsa_posicao()[0]     # Achando a raiz aproximada
c_total = falsa_posicao()[1]             # Achando o número de iterações
x_barra = falsa_posicao()[2]             # Achando a lista de x_barra
x_barra_aplicados = falsa_posicao()[3]   # Achando a lista do x_barra aplicado
valores_a = falsa_posicao()[4]           # Achando a lista de valores de a
valores_b = falsa_posicao()[5]           # Achando a lista de valores de b
a_aplicado = falsa_posicao()[6]          # Achando a lista de valores de a aplicados
b_aplicado = falsa_posicao()[7]          # Achando a lista de valores de b aplicados

print('Questao 01, intervalo [1; 1.25]:')
print(f'A raiz aproximada é: {raiz_aproximada}')
print(f'Para encontrar essa raiz, foram necessárias {c_total} iterações.')

"""# Criando a tabela com os valores obtidos
# Criando o arquivo
outWorkbook = xl.Workbook("Questao_02_2o_intervalo_falsa_posicao.xlsx")
outSheet = outWorkbook.add_worksheet()

# Declarando os títulos

# Escrevendo os dados no arquivo
# .write(location_y, location_x, thing to be written)
outSheet.write("A1", "a")
outSheet.write("B1", "f(a)")
outSheet.write("C1", "b")
outSheet.write("D1", "f(b)")
outSheet.write("E1", "x_barra")
outSheet.write("F1", "f(x_barra)")

for number, item in enumerate(valores_a):
    outSheet.write(number + 1, 0, item)
for number, item in enumerate(a_aplicado):
    outSheet.write(number + 1, 1, item)
for number, item in enumerate(valores_b):
    outSheet.write(number + 1, 2, item)
for number, item in enumerate(b_aplicado):
    outSheet.write(number + 1, 3, item)
for number, item in enumerate(x_barra):
    outSheet.write(number + 1, 4, item)
for number, item in enumerate(x_barra_aplicados):
    outSheet.write(number + 1, 5, item)
outWorkbook.close()"""


tempo_final = time.time()
tempo_gasto = tempo_final - tempo_inicial
print(f'Foram gastos {tempo_gasto}s.')
