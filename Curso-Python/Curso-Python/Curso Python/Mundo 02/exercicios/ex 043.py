'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

from time import sleep

#boas vindas

sleep(0.5)
print('-' *30)
print('Calculo de índice de Massa Corporal (IMC)')



peso = float(input('Inserir o seu peso (Kg): '))
altura = float(input('Inserir a sua altura (m): '))

# convertendo altura para metros caso seja necessário:
if altura > 100:
    altura = altura / 100
else:
    altura = altura

# IMC:

imc = peso / (altura ** 2)
sleep(1)
print(f'Seu indíce de massa corporal (IMC) é {imc:.1f}. Você está: ', end = '')
sleep(0.7)
# Classificação:

if imc < 18.5:
    print('Abaixo do peso.')

elif imc >= 18.5 and imc <= 25:
    print('Com peso ideal.')

elif imc > 25 and imc < 30:
    print('Com Sobreso')

elif imc >= 30 and imc <= 40:
    print('Com obesidade.')

else:
    print('Com obesidade mórbida.')

sleep(1)
print('Para mais informações, sempre busque ajuda profissional para cuidar de sua saúde!')
sleep(1)
print('')
sleep(1)
print('         FIM DO CÁLCULO')
print('-' * 30)
