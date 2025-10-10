# Crie um programa que faça o computador jogar Jokenpô com você.'''

from time import sleep
from random import randint

print('''(1)pedra
(2)Papel
(3)Tesoura''')

sleep(1)
pc = randint(1, 3)
ação = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
jogador = int(input('Inserir a ação desejada: '))

# para evitar erros de digitação:
if jogador not in [1, 2, 3]:
    print('Por favor insira o número indicado para cada ação.')
    exit()

print('-=' * 30)
print('{:^55}'.format('JO'))
sleep(0.5)
print('{:^55}'.format('KEN'))
sleep(0.5)
print('{:^55}'.format('PO!'))
sleep(1)
print('-=' * 30)
# condições
if pc == jogador:
    print(f'EMPATE! Vocês escolheram a ação de {ação[pc]}')

elif jogador == 1 and pc == 3 or jogador == 2 and pc == 1 or jogador == 3 and pc == 2:
    print(
        f'Você VENCEU o computador! Você escolheu {ação[jogador]} e o pc {ação[pc]}! ')
else:
    print(
        f'Você PERDEU! Você escolheu {ação[jogador]} e o pc escolheu {ação[pc]}')

print('-=' * 30)
