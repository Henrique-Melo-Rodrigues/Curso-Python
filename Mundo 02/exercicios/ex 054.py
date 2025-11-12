# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# Mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
# 21 anos, maior de idade, menor que 21, menor de idade.
from datetime import date
for i in range(0, 7):
    nasc = int(input('Inserir ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
