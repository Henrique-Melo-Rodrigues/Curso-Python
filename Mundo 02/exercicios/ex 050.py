# Desenvolva um programa que leia seis numeros inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
soma = 0
for i in range (0, 6):
    n = int(input('Inserir um número: '))
    if n % 2 == 1:
        ação = 'desconsiderado'
    else:
       soma += n
print(f'a soma dos números pares inseridos é {soma}')
print('fim')
