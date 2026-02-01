'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['Nome'] = str(input('Nome do(a) aluno(a): ')).capitalize().strip()
aluno['Média'] = float(input('Média do(a) aluno(a):  '))

if aluno['Média'] >=7:
    aluno['Situação'] = 'Aprovado.'
else:
    aluno['Situação'] = 'Reprovado'
print(f'O nome é igual {aluno["Nome"]}')
print(f'Média igual {aluno["Média"]}')
print(f'Situação igual a {aluno["Situação"]}')

