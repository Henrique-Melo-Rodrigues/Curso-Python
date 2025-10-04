# Crie um programa que faça o computador jogar Jokenpô com você.'''

from time import sleep
from random import randint

print('''(1)pedra
(2)Papel
(3)Tesoura''')

sleep(2)
pc = randint(1, 3)
ação = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
jogador = int(input('Inserir a ação desejada: '))
if jogador > 3:
    print('Por favor insira o número indicado para cada ação.')  # evitando erros
else:
    # condições
    if pc == jogador:
        print(f'Empate. Vocês escolheram a ação de {ação[pc]}')

    elif jogador == 1 and pc == 3 or jogador == 2 and pc == 1 or jogador == 3 and pc == 2:
        print(
            f'Você venceu o computador, ele escolheu {ação[pc]} e você {ação[jogador]}! ')
    else:
        print(
            f'Você perdeu! Você escolheu {ação[jogador]} e o pc escolheu {ação[pc]}')
