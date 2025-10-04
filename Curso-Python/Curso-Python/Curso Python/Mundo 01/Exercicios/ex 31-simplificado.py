dist = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a realizar uma viagem de {dist:.1f}Km.')
preço = dist *0.50 if dist <200 else dist *0.45
print(f'O preço da passagem será de R${preço:.2f}.')
# prefiro realizar de um jeito alternartivo