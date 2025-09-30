#Crie um programa que leia um número inteiro e mostre se ele é par ou impar

n = int(input('insira um número inteiro: '))
if n % 2 ==0: #caso a sobra da divisão seja 0, o número é divisível por 2 e é par
    print(f'O número {n} é par.')
else: #caso sobre número, {n} será impar por não ser divisível por 2
    print(f'O número {n} é impar.')