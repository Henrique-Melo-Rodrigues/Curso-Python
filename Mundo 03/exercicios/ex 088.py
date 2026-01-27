'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.'''
from time import sleep
from random import randint
mega_sena = list()
jogada = list()
contador = 0
print("=" * 30)
print('     Jogando na mega sena        ')
print("=" * 30)
quantidade_de_jogos = int(input('Quantos jogos deseja sortear? '))
while contador <= quantidade_de_jogos:
    for numeros in range(0, 6):
        n = randint(1, 60)
        if n not in jogada:
            jogada.append(n)
        if len(jogada) == 6:
            jogada.sort()
            mega_sena.append(jogada[:])
            jogada.clear()
    contador += 1
print("=" * 40)
print("="*10, f"Sorteando {quantidade_de_jogos} jogos: ", "="*10)

for jogo, indice in enumerate(mega_sena):
    print(f'Jogo {jogo + 1}: {indice}')
    sleep(1)
