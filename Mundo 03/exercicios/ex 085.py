'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numbers = [[],[]] #[0] = par, [1] = impar
for i in range(0,7):
    n=(int(input('Inserir um número: ')))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)
print('-=' *30)
numbers[0].sort()
numbers[1].sort()
print(f'Os valores digitados foram: {numbers}.')
print('Lista 1 == Números pares')
print('Lista 2 == Números ímpares')
