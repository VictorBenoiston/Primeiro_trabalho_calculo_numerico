import numpy as np
import xlsxwriter as xl
import time

# Função utilizada: f(x) = cos(x)+e^x // Intervalo: [-7; 5]// h: 0.5 // Precisão: 10^-7

# Utilizando o método da Secante para o intervalo [-5; -4.5]:

tempo_inicial = time.time()

def test(x):
    x_barra_aplicado = np.cos(x)+np.exp(x)
    return x_barra_aplicado

"""# Achando os dois valores de f(x) com os valores iniciais escolhidos:
x_barra_0 = test(-5)  # 0.2904001
x_barra_1 = test(-4.5)    # -0.1996868"""

def secante():
    c = 2
    x_barra = [-5, -4.5]  # Os dois vlores iniciais são os dois extremos de I
    x_barra_aplicado = [0.2904001, -0.1996868]
    def funcao_iteracao():
        resultado = x_barra[-1] - (x_barra_aplicado[-1] * (x_barra[-1] - x_barra[-2])) / (x_barra_aplicado[-1] - x_barra_aplicado[-2])
        return resultado
    while True:
        x_barra_atual = funcao_iteracao()
        x_barra.append(x_barra_atual)
        x_barra_aplicado_atual = test(x_barra_atual)
        x_barra_aplicado.append(x_barra_aplicado_atual)
        if x_barra_aplicado_atual < 0:
            modulo_x_aplicado_atual = x_barra_aplicado_atual * (-1)
        else:
            modulo_x_aplicado_atual = x_barra_aplicado_atual
        if modulo_x_aplicado_atual < 10 ** -7:
            break
        else:
            c+= 1
    return x_barra[-1], x_barra, x_barra_aplicado, c

raiz_aproximada = secante()[0]
lista_x_barra = secante()[1]
lista_x_aplicado = secante()[2]
iteracoes = secante()[3]

print('Questao teste, intervalo [-5; -4.5]:')
print(f'A raiz aproximada é: {raiz_aproximada}')
print(f'Para encontrar essa raiz, foram necessárias {iteracoes} iterações.')
print(lista_x_barra)
print(lista_x_aplicado)

"""# Criando a tabela com os valores obtidos
# Criando o arquivo
outWorkbook = xl.Workbook("Questao_01_1o_intervalo_secante.xlsx")
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
