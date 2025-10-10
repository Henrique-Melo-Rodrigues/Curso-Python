from time import sleep
print('Reajustando o seu sálario...')
sleep(1)
salário = float(input('Inserir o seu salário atual: '))
if salário >1518: #salário mínimo de 2025
    reajuste = salário+(salário*(10/100))
else:
    reajuste = salário+(salário*(15/100))
print(f'com o reajuste salarial, o seu salário passará de R${salário:.2f} para R${reajuste:.2f}')

