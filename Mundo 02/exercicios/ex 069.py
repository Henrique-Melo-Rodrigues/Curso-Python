adultos = 0
homens = 0
moças = 0
while True:
    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >18:
        adultos +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        moças +=1
    print('-'*20)

    opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
        print('-'*20)
print(f'Total de pessoa com mais de dezoito anos: {adultos}.')
print(f'ao todo temos {homens} homens cadastrados.')
print(f'E temos {moças} com menos de 20 anos.')
