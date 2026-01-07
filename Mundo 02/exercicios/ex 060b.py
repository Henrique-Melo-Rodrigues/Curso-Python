n = int(input('Inserir um número: '))
f = 1
for c in range(n, 1, -1):
    f *= c
    print(f'{c}', end='')
    print(' x ', end='')
print(f'{f}')
