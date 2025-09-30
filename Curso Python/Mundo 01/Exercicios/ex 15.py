km= float(input('Quantidade de km rodado: '))
diaria= int(input('Quantidade de dias com o carro alugado: '))
custo_por_km= 0.15
custo_por_dia= 60
preco_km= km * custo_por_km
preco_dia= diaria*custo_por_dia
print(f'O preço total a se pagar do aluguel do carro será de R${preco_km+preco_dia:.2f}')
