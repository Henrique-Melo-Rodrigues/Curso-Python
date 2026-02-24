'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
SomaIdade = MediaIdade = 0
galera = list()
pessoa = dict()
mulheres = list()
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    sexo = str(input(f'Sexo de {pessoa["Nome"]} (M/F): ')).strip().upper()[0]
    while sexo not in ('M', 'F'):
        print('Opção inválida.')
        print('Escreva somente [M/F]')
        sexo = str(
            input(f'Sexo de {pessoa["Nome"]} (M/F): ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(pessoa['Nome'])
        sexo = 'Feminino'
    if sexo == 'M':
        sexo = 'Masculino'
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input(f'Idade de {pessoa["Nome"]}: '))
    SomaIdade += pessoa['Idade']
    galera.append(pessoa.copy())
    escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while escolha not in ('S', 'N'):
        print('Opção inválida.')
        print('Escreva somente [S/N]')
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'A) Ao todo, temos Pessoas {len(galera)} cadastradas:')
MediaIdade = SomaIdade / (len(galera))
print(f'B) A média de idade dos registrados é de {MediaIdade:5.2f} anos.')
print(f'C) Um total de {len(mulheres)} Mulheres registradas: ',end='')
for mulher in mulheres:
    print(f'{mulher};',end=' ')
print()
print(f'D) Lista de pessoas acima da média: ',end='')
for p in galera:
    if p['Idade'] >=MediaIdade:
        print('    ',end='')
        for keys, values in p.items():
            print(f'{keys} = {values};',end='')
        print()
print('<<ENCERRADO>>')
