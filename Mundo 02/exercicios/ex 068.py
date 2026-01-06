from random import randint
from time import sleep
cont = 0
while True:
    print('-='*10, 'Jogo do PAR ou ÍMPAR!', '=-'*10)
    n = int(input('Inserir um número: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    sleep(0.5)
    while escolha in 'PI':
        pc = randint(1,10)
        soma = pc + n
        if soma % 2 == 0:
            resultado = 'PAR'[0]
            print(f'A soma entre a sua escolha e a minha é {soma}. E o número {soma} é par...')
            sleep(0.5)
            if escolha == resultado:
                print(f'Você venceu!')
                cont += 1
                break
            else:
                print(f'Você perdeu! Você ganhou {cont} vezes.')
                break
        else:
            resultado = 'IMPAR'[0]
            print(f'A soma entre a sua escolha e a minha é {soma}. E o número {soma} é impar...')
            sleep(0.5)
            if escolha == resultado:
                print('Você venceu! ')
                cont += 1
            else:
                print(f'Voce perdeu! você ganhou {cont} vezes')
            break
    if resultado != escolha:
        print('-='*31)
        break
    else:
        print('Vamos jogar denovo!')
print('FIM')
