from random import randint
'''n1 =  randint(1,10)
n2 =  randint(1,10)
n3 =  randint(1,10)
n4 =  randint(1,10)
n5 = randint(1,10)'''
aleatório = (randint(1, 10), randint(1, 10), randint(1, 10),
             randint(1, 10), randint(1, 10))
print(f'Os valores gerados foram:', end=' ')
for n in aleatório:
    print(n, end=' ')
print(f'\nO maior valor gerado foi {max(aleatório)}')
print(f'O menor valor gerado foi {min(aleatório)}')
