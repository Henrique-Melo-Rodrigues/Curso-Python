#para manter o nome sem '   ' desnecessários:
name= str(input('Inserir o seu nome completo: ')).strip()
split = name.split() #separando o nome em lista
print('Analisando o seu nome...')
print(f'o seu nome em letras maiúsculas é: {name.upper()}') #.upper()=maiúsculas
print(f'Seu nome totalmente em letras minúsculas: {name.lower()}') #.lower()= minúsculas

#correção na que eu estava tendo dificuldades:
print('O seu nome tem um total de {} letras'.format(len(name)- name.count(' ')))
#Analise da correção: (f'alguma coisa') facilita muito, mas para variáveis mais complexas é melhor usar o .format


#minha forma de saber quantas letras tem o primeiro nome:
print(f'Seu primeiro nome tem um total de {len(split[0])} letras')

#forma do guanabara:
print('O seu primeiro nome tem {} letras'.format(name.find(' ')))
