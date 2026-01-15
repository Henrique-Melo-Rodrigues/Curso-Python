numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))

print(f'Você digitou os números:', end=' ')
for n in numero:
    print(n, end= ' ')
print(f'\nO Número 9 apareceu {(numero.count(9))} vezes;')
if 3 in numero:
    print(f'O primeiro número três foi digitado na {(numero.count(3) + 1)}° posição;')
else:
    print('O número 3 não foi digitado nenhuma vez;')
print(f'Os números pares foram: ', end=' ')
for pares in numero:
    if pares % 2 == 0:
        print(pares, end= ' ')


