adultos = moças = homens = 0
while True:
    idade = int(input('Idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo da pessoa [M/F]: ')).strip().upper()[0]
    opção = ' '
    if sexo == 'M':
        homens +=1
    if idade >18:
        adultos +=1
    if sexo == 'F' and idade < 20:
        moças +=1
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        print('-'*20)
        break
    print('-'*20)
print(f'Total de pessoa com mais de dezoito anos: {adultos}.')
print(f'ao todo temos {homens} homens cadastrados.')
print(f'E temos {moças} mulheres com menos de 20 anos.')
