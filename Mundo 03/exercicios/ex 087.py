'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
pares = maior_da_linha_dois = soma_coluna_tres  = 0
matriz =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Inserir valor para a posição [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é igual a {pares}.')

for l in range(0,3):
    soma_coluna_tres += matriz[l][2]
print(f'A soma da coluna três é {soma_coluna_tres}.')

for l in range(0,3):
    if c == 0:
        maior_da_linha_dois = matriz[1][c]
    elif matriz[1][c] > maior_da_linha_dois    :
            maior_da_linha_dois = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_da_linha_dois}.')
