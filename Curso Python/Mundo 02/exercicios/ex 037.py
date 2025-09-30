# Exercicio 037 - Conversor de Bases Numéricas
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# Mostre o número escolhido na base correspondente.

from time import sleep

sleep(1)
print('-'*20)
sleep(1)
print('iniciando programa')
sleep(0.5)

n=int(input('inserir um número inteiro:  '))
print('''Escolha uma das bases para conversão:
[ 1 ]- binário
[ 2 ]- Octal
[ 3 ]- Hexadecimal''')
escolha = int(input('sua escolha: '))

if escolha == 1:
    binario = bin(n)
    print(f'{n} convertido para binário é igual a {binario[2:]}')
elif escolha == 2:
    octal = oct(n)
    print(f'{n} transformado em octal é igual a {octal[2:]}')
elif escolha == 3: 
    hexa =hex(n)
    print(f'{n} em forma hexadecimal é {hexa[2:]}')
else:
    print('Por favor inserir apenas uma das três opções acima: ')

sleep(2)
print('Fim do programa')
sleep(1)
print('-'*20)


