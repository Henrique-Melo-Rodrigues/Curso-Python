# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Contagem regressiva para a queima de fogos de artifício em: ')
for c in range(0, 11):
    sleep(1)
    print(c)
sleep(1)
print('\033[1;31mBarulho de explosão de fogos!\033') #Adicionando cor no print

