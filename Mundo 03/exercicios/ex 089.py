'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.'''
aluno = list()
while True:
    nome = (str(input('Nome do(a) aluno(a): ')).capitalize().strip())
    nota1 = (float(input('Inserir nota 1: ')))
    nota2 = (float(input('Inserir nota 2: ')))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if escolha == 'N':
        break
print("-" * 40)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)
for posicao, a in enumerate(aluno):
    print(f'{posicao:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*30)
    opc = int(
        input("Deseja mostrar a nota de qual aluno? (999 finaliza o programa) "))
    if opc == 999:
        print('Desligando o programa...')
        break
    if opc <= len(aluno) - 1:
        print(f"Notas de {aluno[opc][0]} são {aluno[opc][1]}")
print('Volte sempre!')
