# Condicionais
# if, elif e else
'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso
ao contrario irá tomar uma suspensão.
'''

numero_de_atrasos = 4
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, será suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais 1 falta, será suspenso')
else:
    print('Pode entrar')