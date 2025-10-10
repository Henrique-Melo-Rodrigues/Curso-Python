num = int(input('Inserir um número: '))
n = str(num)
print(f'Analisando o número {n}...')
print(f'Dividirei o {n} em casas decimais:')
print(f'Unidade: {(n[3])}') #unidade é sempre o´último número à esquerda
print(f'Dezena: {(n[2])}')
print(f'Centena: {(n[1])}')
print(f'milhar: {(n[0])}')

#não está calculando números pequenos
#passo 1: transformar n em int
#passo 2: criar uma condição para n e transformá-lo em string
#passo 3: criar uma lista na condição de string
