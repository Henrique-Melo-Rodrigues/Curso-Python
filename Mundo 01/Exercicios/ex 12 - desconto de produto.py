camisa = float(input('Insirir o valor do produto: R$ '))
desconto = (camisa * 5/100) #5/100 é 5%. simples assim!
valor= camisa-desconto
print(f'Aplicando um desconto de 5% sobre a camisa, que antes custava R${camisa:.2f} passará a ter um valor de R${valor:.2f} . ')


