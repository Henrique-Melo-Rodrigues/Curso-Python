nome = str(input('inserir o seu nome: ')).strip().title()
n = nome.split()
print('Muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(n[0])) # primeiro nome vai estar na lista 0
#Identificando o último nome sem saber o tamanho da lista:
print('Seu último nome é {}'.format(n[len(n)-1])) #<<-- prestar atenção no código
