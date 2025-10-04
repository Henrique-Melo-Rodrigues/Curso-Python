f = str(input('escreva uma frase: ')).strip().lower()
count = f.count('a')
quando = f.find('a')
fim = f.rfind('a') #procura o 'A' da direita para a esquerda
print(f'Analisando a frase..')
print(f'A letra aparece {count} vezes.')
print(f'A primeira letra A apareceu na posição {quando+1}')
print(f'A última letra A apareceu na posição {fim}')


