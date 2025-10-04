print('--------Radar eletrônico--------')
print('A quantos km/h você estava dirigindo ontem?')
km = float(input('Velocidade do carro em km/h: '))

if km > 80:
    print('Você será multado você ultrapassou o limite permitido de 80km/h!')
    print('O valor da multa será de R${:.2f}'.format((km-80)*7))
else:
    print('Você está respeitando as normas de trânsito. Continue assim!')
print('Sempre dirija com segurança!')
print('-------------------------------')

