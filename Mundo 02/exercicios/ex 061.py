#Input:
a1 = int(input('Inserir o primeiro termo da PA: '))
r = int(input('Razão da PA: '))

#Validação de dados:
termo = a1
contador = 1

#loop:
while contador <= 10:
    print(termo, end='  →  ')
    termo += r
    contador += 1
print('FIM')
