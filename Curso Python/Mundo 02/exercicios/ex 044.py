'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros'''

from time import sleep
print('-'*30)
sleep(0.9)
print('         CALCULADORA DE VALOR A SER PAGO')
sleep(2)

valor = float(input('Valor a ser pago: '))
sleep(2)
print('''Qual a forma de pagamento?
    (1) À vista dinheiro/cheque
    (2) À vista no cartão
    (3) Em até 2x no cartão
    (4) 3x ou mais no cartão''')
forma_de_pagamento = int(input('Inserir opção (de 1 a 4): '))
if forma_de_pagamento > 4:  # evitando erros na escolha da opção
    print('Por favor, insira apenas os números que contém opção.')

sleep(1)
# condições:

if forma_de_pagamento == 1:
    desconto = valor - (valor*0.1)
    print(f'Pagamento a vista recebe desconto no pagamento!\
o valor a ser pago será de R${desconto:.2f}')

elif forma_de_pagamento == 2:
    desconto = valor - (valor * 0.05)
    print(f'Pagamento a vista recebe desconto no pagamento!\
O valor a ser pago será de R${desconto:.2f}')

elif forma_de_pagamento == 3:
    pag = valor / 2
    print(f'O valor a ser pago será de duas parcelas de R${pag:.2f}')

else:
    juros = valor + (valor * 0.2)  # 20% de juros
    print('O valor a ser pago a partir de 3x no cartão será de 20%')
    parcelas = int(input('Vezes a ser parcelado (em até 10x): '))
    pag = juros / parcelas
    print(
        f'O total a ser pago em cada uma das {parcelas} parcelas será de R${pag:.2f}.')
