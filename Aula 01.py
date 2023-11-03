# Variaveis
velocidade_internet = 10
print(velocidade_internet)
# Numeros
nota_filme = 8.5 #float
# Valores_boleanos
esta_aberto  = True
# Strings
nome_do_curso = 'Logica de programação'

# Como variaveis seriam usadas na vida real?
# Problema 1 - valor por hora
# Escreva um programa que retorna o valor hora de um funcionario com base no seu salario mensal e horas trabalhas por mês.

''''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''

salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês?')
valor_hora = int (salario_mensal) / int (horas_trabalhadas_por_mes)
print(valor_hora)