from random import choice
n1 = input('Nome do(a) primeiro aluno(a): ')
n2 = input('nome do(a) segundo aluno(a): ')
n3 = input('nome do(a) terceiro aluno(a): ')
n4 = input('nome do(a) quarto aluno(a): ')
alunos= [n1, n2, n3, n4] #criar uma lista com colchetes
sorteio = choice(alunos)

print(f'o sorteado a apagar o quadro será o(a) aluno(a): {sorteio}!')



