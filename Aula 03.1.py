# Laços de Repetição + Listas
# Problema 1 a N - imprime os valores de 1 a N
'''
Input numero maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
    print valor
'''

valor_maximo = int (input('Digite o valor maximo'))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1):
    print(numero)