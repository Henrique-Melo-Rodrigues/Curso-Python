dist = float(input('Distância que será percorrida (em km): '))
print(f'Você realizará uma viagem de {dist}Km.')
if dist <=200:
    print(f'O valor a ser pago será de RS${(dist*0.5):.2f}')
else:
    print(f'O valor a ser pago será de R${(dist*0.45):.2f}')
