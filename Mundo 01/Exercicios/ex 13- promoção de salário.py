funcionario= input('nome do funcionário: ')
salario= float(input(f'Salário do(a) {funcionario}: R$ '))
promocao= salario+(salario*(15/100))
print(f'Graças a promoção salarial de 15% do(a) funcionário(a) {funcionario},\no seu pagamento de R${salario:.2f} será reajustado para um salário de R${promocao:.2f}.')