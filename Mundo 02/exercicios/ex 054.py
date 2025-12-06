# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# Mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
# 21 anos, maior de idade, menor que 21, menor de idade.
from datetime import date
maior_idade = 0
menor_idade = 0
for i in range(1, 8):
    nasc = int(input(f'Inserir ano de nascimento da {i}° pessoa: '))
    ano = date.today().year
    idade = ano - nasc
    if idade >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'O número de pessoas maiores de idade é {maior_idade} e o de menores de idade é {menor_idade}')
