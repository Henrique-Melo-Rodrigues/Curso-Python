nome=input('inserir nome do aluno: ')
rm=input('inserir rm do aluno: ')
sala=input('inserir sala do aluno: ')
bimestre=input('inserir bimestre: ')
matematica=int(input('inserir nota do aluno em matemática: '))
portugues=int(input('inserir nota em português: '))
fisica=int(input('inserir nota em física: '))
ingles=int(input('inserir nota em inglês: '))

media=int((matematica+portugues+fisica+ingles)/4)
print('O(A) aluno(a) {},\n do RM:{}, da sala {}, teve uma média de nota de {}\n no {}.\n -Escola Pipipi Popopo, 2025'.format(nome,rm,sala,media,bimestre))

