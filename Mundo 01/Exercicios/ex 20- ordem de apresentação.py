import random
a1 = str(input('Nome do(a) lider do primeiro grupo: '))
a2 = str(input('Nome do(a) lider do segundo grupo: '))
a3 = str(input('Nome do(a) lider do terceiro grupo: '))
a4 = str(input('Nome do(a) lider do quarto grupo: '))
apresentação = [a1,a2,a3,a4]
numero= random.sample(apresentação, 4)
print(f'a ordem de apresentação será:\n{numero}')

