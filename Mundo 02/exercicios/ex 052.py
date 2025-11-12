# faça um programa que leia um numero inteiro e mostre na tela se ele é primo ou nao.
n = int(input('Inserir um número inteiro: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end ='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')
print(f'\n\033[0mO número {n} foi dividido {total} vezes.')
if total == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')
