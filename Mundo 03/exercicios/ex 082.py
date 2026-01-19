'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
par = []
impar = []
cont = 0
while True:
    cont += 1
    n = int(input(f'Inserir o {cont}° Número: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    escolha = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    while escolha not in 'SsNn':
        print('Opção inválida. ')
        escolha = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    if escolha == 'N':
        break
print('-=' * 30)
print(f'Os números inseridos foram: {numeros};')
if len(par) > 0:
    print(f'Os números pares obtidos foram: {par}')
else:
    print('Não foi computado nenhum número par.')
if len(impar) > 0:
    print(f'Já os ímpares computados: {impar}')
else:
    print('Não foi computado nenhum número ímpar.')
