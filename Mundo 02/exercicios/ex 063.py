n = int(input('Inserir termo da fibonnaci: '))
t1 = 0
t2 = 1
an = 3
print(f'{t1} -> {t2}', end=' ')
while an < n: #Contador e número de termos
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    an += 1
    print(f'-> {t3}', end=' ')
print('FIM')
