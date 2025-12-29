n = cont = soma = 0
n = int(input('Inserir um valor [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Inserir um valor [999 para parar]: '))
print(f'Você digitou {cont} números.',end =' ')
print(f'E a soma de todos os valores digitados, com excessão do número 999, foi de {soma:.0f}')
