# faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f'Inserir o peso da {i}° pessoa em (KG): '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso entre as 5 pessoas é de {maior}Kg e o menor possuí {menor}Kg')
