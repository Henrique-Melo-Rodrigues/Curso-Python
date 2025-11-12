# refaça o exercicio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.
from time import sleep

n = int(input('Inserir o número que deseja ver a tabuada: '))
sleep(1)
for i in range(1, 11):
    print(f'{n} x {i} = {i * n}')
    sleep(0.25)
sleep(0.5)
print('Fim')
