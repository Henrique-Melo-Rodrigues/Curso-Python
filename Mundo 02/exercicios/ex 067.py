from time import sleep

while True: # Controla a quantidade de vezes que o N irá aparecer
    n = int(input('Inserir um número para ver a sua tabuada [números negativos encerram o programa  ]: '))
    if n <0:
        print('PROGRAMA ENCERRADO. VOLTE SEMPRE')
        print('-'*20)
        break

    cont = 1 #Contador sempre começará com 1 para fazer o primeiro produto da tabuada.
    while True:
        produto = n * cont
        print(f'{n} x {cont} = {produto}')
        sleep(0.25)
        cont +=1
        if cont > 10: # Contador maior que 10: volta para o While exteno
            print('-'*20)
            break
    print('-'*20)
print('Fim do programa')

#While externo = controla a quantidade de vezes que irá repetir o programa
#While interno = possuí a lógica principal do programa, que é fazer a tabuada do input entre 1 e o 10.
