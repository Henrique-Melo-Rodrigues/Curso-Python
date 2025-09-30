    #classificando variavel como string e chamando a função .title
        #Funcão .title para por a primeira letra em maiúscula

nome = str(input('Inserir o seu nome: ')).title() 
if nome == 'Henrique':
    print(f'Que nome bonito hein, {nome}!')
elif nome == 'Pedro' or nome=='Maria' or nome=='Enzo' or nome=='Paulo':
    print(f'{nome} é um nome bem famoso no Brasil.')
elif nome == 'Clorivaldo':
    print(f'Que nome diferenciado hein, {nome}...')
elif nome in 'Joaquim Miguel Vinicius Gustavo':
    print(f'Nome bonito, {nome}')
else:
    print(f'bom nome hein, {nome}')
print(f'Tenha um bom dia, {nome}!')
