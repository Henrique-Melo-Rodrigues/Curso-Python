a = [2, 3, 4, 7]
b = a #Cria uma ligação entre ambas as listas e não copiacd 
c = a[:] #Cópia dos valores
c[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista copiada do A: {c}')
