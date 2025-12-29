from random import randint
from time import sleep

print('-='*10, 'Iniciando o sorteio', '-='*10)
sleep(1)
print('O computador escolheu um número entre 0 e 10.\nAcerte que número foi escolhido!') #Contextualização
sleep(1)

pc = randint(0,10)
tentativas = 0
acertou = False
while not acertou:
    n = int(input('Inserir o número que o PC computou [DE 0 A 10]: '))
    if n != pc:
        tentativas += 1
        sleep(1)
        print(f'Você errou! tente novamente')
        if n > pc:
            print('Menos... tente novamente.') #o número escolhido pelo pc é menor do que o inserido pelo usuário.
        else:
            print('Mais... tente novamente.') #O número computado é maior do que o número que o usuário digitou.
    else:
        acertou = True
        tentativas += 1
        if tentativas == 1:
            print(f'VOCÊ ACERTOU DE PRIMEIRA! o pc escolheu o número {pc} e você também!')
        else:
            print(f'VOCÊ ACERTOU NA {tentativas}° tentativa! você e o pc escolheram o número {pc}')
sleep(1)
print('-='*10, 'Fim', '-='*10)

