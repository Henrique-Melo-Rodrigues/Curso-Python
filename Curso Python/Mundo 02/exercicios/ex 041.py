'''A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 25 anos: Sênior
- Acima de 25 anos: Master'''

from time import sleep
from datetime import date

print('-'*40)
sleep(1)

print('''Bem vindo a competição de natação!

        Insira a sua idade abaixo para sabermos em qual categoria o alocar:''')

sleep(1)

i = int(input('Inserir o seu ano de nascimento: '))

ano = date.today().year
c = ano - i
# Transformando o ano de nascimento para uma idade

sleep(1)
if c >=0 and c<=100: #Criando um limitador de idades para evitar erros de digitação

    print('Computando...')
    sleep(1)

    print(f'Você tem {c} anos...')
else:
    print('Computando...')
    print('Você pode ter digitado o ano de nascimento errado. Por favor reenviar o formulário.')

sleep(0.5)

if c <= 9:
    print('Você irá competir na categoria mirim.')

elif c > 9 and c <= 14:
    print('Você irá competir na categoria infantil.')

elif c > 14 and c <= 19:
    print('Você irá competir na categoria júnior')

elif c > 19 and c <= 25:
    print('Você irá competir na categoria Sênior.')

elif c > 25:
    print('Você irá competir na categoria Master.')
