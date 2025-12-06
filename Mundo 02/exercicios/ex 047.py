# Crie um programa que mostre na tela todos os nmeros pares que estao no intervalo entre 1 e 50.
from time import sleep
print('Todos os números pares entre 1 e 50: ')
for c in range(2, 51, 2): # do 1 até o 50 pulando de 2 em 2
    print(c, end=' ')
    sleep(0.25)
sleep(0.5)
print('Fim!')
