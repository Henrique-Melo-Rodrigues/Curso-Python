dias= int(input('Quantidade de dias alugados: '))
km= float(input('Quantidade de km rodados: '))
custos= (dias* 60) + (km * 0.15) #60 é a diaria e R$0.15 é por km rodado
print(f'O valor final a se pagar será de R${custos:.2f}.')