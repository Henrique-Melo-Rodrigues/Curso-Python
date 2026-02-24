'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
from time import sleep
jogador = dict()
gols = list()

jogador['Nome'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range(0, partidas):
    partida = int(input(f'Quantos gols na partida {p+1}? '))
    gols.append(partida)
jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)
print(jogador)
print('-=' * 30)
for keys, values in jogador.items():
    print(f' - O campo {keys} tem o valor {values}.')
print('-=' * 30)

print(f'O jogador {jogador["Nome"]} Jogou {len(jogador["Gols"])} partidas.')
for indice, values in enumerate(jogador['Gols']):
    print(f'  ==> Na partida {indice + 1}, fez {values} gols.')
    sleep(1)
print(f'Foi um total de {jogador["Total de gols"]} gols.')
print('-=' * 30)
