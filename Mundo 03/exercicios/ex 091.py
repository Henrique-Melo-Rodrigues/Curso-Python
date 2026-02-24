'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios.Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
ranking = list()
print('=-' * 19)
print("Valores sorteados: ")
for k, v in jogos.items():
    print(f'O {k} tirou o número {v} no dado.')
    sleep(1)
print('=-' * 19)
print('=-' * 6, 'RESULTADOS', '=-' * 6)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i ,v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(0.5)
