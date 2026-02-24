'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
pessoa = dict()
pessoa['Nome'] = str(input("Inserir nome: ")).capitalize().strip()
Sexo = str(input(f'Sexo de {pessoa["Nome"]} [M/F]: ')).upper().strip()[0]
while Sexo == '' or Sexo[0] not in ('M','F'):
    print('Opção inválida.')
    Sexo = str(input(f'Sexo de {pessoa["Nome"]} [M/F]: ')).upper().strip()
pessoa['Sexo'] = Sexo[0]
ano = int(input(f'Ano de nascimento do(a) {pessoa["Nome"]}: '))
idade = (date.today().year) - ano
pessoa['Idade'] = idade
pessoa['ctps'] = int(input('Numero da carteira de trabalho [digitar "0" se não tiver CTPS]: '))

if pessoa['ctps'] != 0:
    pessoa['Contrato'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    if pessoa['Sexo'] == 'F':
        pessoa['Aposentadoria'] = pessoa['Idade'] + ((30 + pessoa['Contrato']) - date.today().year)
    if pessoa['Sexo'] == 'M':
        pessoa['Aposentadoria']  = pessoa['Idade'] + ((35 + pessoa['Contrato']) - date.today().year)

if pessoa['Sexo'] == 'M':
    pessoa['Sexo'] = 'Masculino'
if pessoa['Sexo'] == 'F':
    pessoa['Sexo'] = 'Feminino'
print('-=' * 15)
for keys, values in pessoa.items():
    print(f'  - {keys} tem valor: {values}')

