# Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três# e que se encontram no intervalo de 1 até 500.
from time import sleep
soma = 0
cont = 0
print('Todos os números ímpares no intervalo de 1 até 500: ')
for i in range(1, 501, 2):
    if i % 3 == 0:  # se sobrar 0, é um multiplo de 3.
        print(i, end=' ')
        sleep(0.05)
        soma += i
        cont += 1
sleep(1)
print('\n'f'A Soma de todos {cont} valores solicitados que são ímpares e múltiplos do 3 entre o 1 e 500 é {soma:.0f}')


