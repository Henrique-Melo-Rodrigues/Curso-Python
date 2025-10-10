'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

from time import sleep

print('-'*10)

sleep(1)
print('Começando programa')
sleep(1)
n1 = int(input('Inserir um número: '))
print('-'*10)
print('computando...')
sleep(1.5)
n2 = int(input('Inserir outro número: '))

if n1 == n2:
    print(f'não existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior.')

sleep(1)
print('Fim')
print('-'*10)
