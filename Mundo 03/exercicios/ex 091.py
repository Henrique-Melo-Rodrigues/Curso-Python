'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios.Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
jogadas = dict()
jogador = list()
for c in range(1,5):
    jogadas['Jogador'] = f'{c}'
    jogadas['Dado'] = randint(1, 6)
    jogador.append(jogadas.copy())

for situação in jogador:
    for c, v in situação.items():
        print(f'O {c} {v['Jogador']} tirou {v['Dado']}')
