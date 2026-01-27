matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(
            input(f'Inserir valor para a posição [{l}, {c}] da matriz: '))
        soma += (matriz[l][2])
        if matriz[l][c] % 2 == 0:
            pares += (matriz[l][c])
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares na matriz é {pares}.')
print(f'A soma dos valores na coluna 3 é igual a {soma}')
print(f'O maior valor da linha 2 é {max(matriz[1])}')
