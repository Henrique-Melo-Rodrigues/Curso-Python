n=int(input('Inserir número para calcular a sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
#o {:2} foi utilizado para alinhar a tabuada, fazendo assim, o 10 ficar alinhado com os demais números
#print com .format facilita os códigos.

print('informações adicionais: {}² = {}\nE raiz quadrada de {} = {:.2f}'.format(n, pow(n, 2),n, pow(n,(1/2)))) #pow é igual à potência
print('-'*12) #usar para enfeitar a run.



