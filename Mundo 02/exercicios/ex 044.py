'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros'''

from time import sleep
print('{:=^40}'.format(' CALCULADORA DE VALOR A SER PAGO '))
sleep(1)

valor = float(input('Valor a ser pago: '))
sleep(1)
print('''Qual a forma de pagamento?
    (1) À vista dinheiro/cheque
    (2) À vista no cartão
    (3) Em até 2x no cartão
    (4) 3x ou mais no cartão''')
forma_de_pagamento = int(input('Inserir opção (de 1 a 4): '))

# evitando erros na escolha da opção:

if forma_de_pagamento == 0 or forma_de_pagamento > 4:
    print('Por favor, insira apenas os números que contém opção.')
else:
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
        print(f'O valor a ser pago será de duas vezes sem juros de R${pag:.2f}')

    else:
        juros = valor + (valor * 0.2)  # 20% de juros
        print('O valor a ser pago a partir de 3x no cartão terá um juros de 20% sobre o valor!')
        parcelas = int(input('Vezes a ser parcelado (em até 10x): '))
        pag = float (juros / parcelas)
        print(f'O total a ser pago em cada uma das {parcelas} parcelas será de R${pag:.2f}. ', end='')
        print(f'O valor final a ser pago será de R${juros:.2f}!')

