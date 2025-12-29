n1 = int(input(f'Inserir o 1° valor: '))
n2 = int(input(f'Inserir o 2° valor: '))
c = 0
while c != 5:
    print('''O que deseja fazer com os números acima?
    [  1  ] Somar
    [  2  ] Multiplicar
    [  3  ] Maior
    [  4  ] Novos números
    [  5  ] Sair do programa''')
    c = int(input('Inserir o que deseja fazer: '))
    if c == 1:
        print(f'{n1} + {n2} = {(n1 + n2)}')
    elif c == 2:
        valor = (n1 * n2)
        print(f'{n1} x {n2} = {valor}')
    elif c == 3:
        if n1 > n2:
            maximo = n1
        else:
            maximo = n2
        print(f'o maior valor entre {n1} e {n2} é {maximo}')
    elif c == 4:
        n1 = int(input(f'Inserir o 1° valor: '))
        n2 = int(input(f'Inserir o 2° valor: '))
    elif c == 5:
        print('Finalizando...')
    else: #evitando erros do usuário
        print('Por favor insira apenas os números acima.')

print('=-'*20,'Fim','=-'*20)
