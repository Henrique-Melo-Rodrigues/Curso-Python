from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você ganhou {v} vezes.')
