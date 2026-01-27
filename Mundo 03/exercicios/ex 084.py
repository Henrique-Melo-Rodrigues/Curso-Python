'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
menor = maior = 0
pessoas = []
cadastro = []

while True:
    cadastro.append(str(input('Nome do usuário: ')).capitalize().strip())
    cadastro.append(float(input('Peso do usuário: ')))
    pessoas.append(cadastro[:])
    if len(pessoas) == 1:
        menor = maior = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        elif cadastro[1] < menor:
            menor = cadastro[1]
    cadastro.clear()

    escolha = (str(input('Deseja continuar? [S/N]')).upper().strip())
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = (str(input('Deseja continuar? [S/N]')).upper().strip())
    if escolha == 'N':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso inserido foi {maior}Kg peso de:', end='')
for peso in pessoas:
    if peso[1] == maior:
        print(f'[{peso[0]}]', end='')
print()
print(f'O menor peso inserido foi {menor}Kg peso de:', end=' ')
for peso in pessoas:
    if peso[1] == menor:
        print(f'[{peso[0]}]', end=' ')
