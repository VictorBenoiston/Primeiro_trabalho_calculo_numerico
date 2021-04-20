import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter as xl
import time

# Função utilizada: f(x) = 3 cos(x) - e^x/3 // Intervalo: [-5; 2]// h: 0.75 // Precisão: 10^-5

tempo_inicial = time.time()

"""# Plotando o gráfico, e isolando as raizes:
x = np.arange(-5, 2, 0.75)
print(x)
plt.plot(x, 3*np.cos(x) - np.exp(x) / 3)
plt.show()"""

# Utilizando o método da bisseccao para o intervalo [1; 1.75]:


def test(x):
    valor_aplicado = (3*np.cos(x) - np.exp(x) / 3)
    return valor_aplicado


def bisseccao():
    c = 0
    valores_a = [1]  # Valores positivos
    valores_b = [1.75]  # Valores negativos
    x_barra_aplicados = []
    x_barra = []
    while True:
        x_barra_atualizado = (valores_a[-1] + valores_b[-1]) / 2
        x_barra.append(x_barra_atualizado)
        validacao = test(x_barra[-1])
        if validacao < 0:
            modulo_validacao = validacao * (-1)
            valores_b.append(x_barra_atualizado)
            valores_a.append(valores_a[-1])
        else:
            modulo_validacao = validacao
            valores_a.append(x_barra_atualizado)
            valores_b.append(valores_b[-1])
        if modulo_validacao < 10 ** -5:
            x_barra_aplicados.append(validacao)
            break
        else:
            x_barra_aplicados.append(validacao)
            c += 1
    raiz_aproximada = f'{x_barra[-1]:.5f}'
    return raiz_aproximada, c, x_barra, x_barra_aplicados, valores_a, valores_b


raiz_aproximada_bissecao = bisseccao()[0]
c_total = bisseccao()[1]
print('Questao 02, intervalo [1; 1.75]:')
print(f'A raiz aproximada é: {raiz_aproximada_bissecao}')
print(f'Para encontrar essa raiz, foram necessárias {c_total} iterações.')


"""# Criando a tabela com os valores obtidos
# Criando o arquivo
outWorkbook = xl.Workbook("Questao_03_3o_intervalo_bisseccao.xlsx")
outSheet = outWorkbook.add_worksheet()

# Declarando os dados:
valores_a = bisseccao()[4]
valores_b = bisseccao()[5]
x_barra_list = bisseccao()[2]
x_barra_aplicado = bisseccao()[3]

# Declarando os títulos

# Escrevendo os dados no arquivo
# .write(location_y, location_x, thing to be written)
outSheet.write("A1", "a")
outSheet.write("B1", "b")
outSheet.write("C1", "x_barra")
outSheet.write("D1", "f(x_barra)")

for number, item in enumerate(valores_a):
    outSheet.write(number + 1, 0, item)
for number, item in enumerate(valores_b):
    outSheet.write(number + 1, 1, item)
for number, item in enumerate(x_barra_list):
    outSheet.write(number + 1, 2, item)
for number, item in enumerate(x_barra_aplicado):
    outSheet.write(number + 1, 3, item)
outWorkbook.close()"""

tempo_final = time.time()
tempo_gasto = tempo_final - tempo_inicial
print(f'Foram gastos {tempo_gasto}s.')
