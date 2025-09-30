# Escreva um progama para aprovar o empréstimo bancário para a compra de uma casa.
# o programa vai perguntar o Valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o valor será negado.

from time import sleep  # importando delay para o programa

# title para nomes e strip para colocar espaçador de forma exata.
nome = str(input('Inserir seu nome: ')).title().strip()
sleep(0.5)

print(f'Olá, {nome}, façamos uma verificação do seu pedido de empreśtimo...')
sleep(0.5)

print('Para isso, preencha as perguntas a seguir: ')
sleep(1)

valor = float(input('inserir o valor da casa: R$ '))
salário = float(input('inserir o seu salário: R$ '))
anos = int(input('Em quantos anos será pago a prestação: '))

#Transfomando anos para meses:
meses = int (anos *12)

#prestação mensal:
prest = (valor/meses) #Porcentagem da prestação mensal sobre o salário e a quantidade de anos a ser pago
minimo = salário*30 / 100


#Condições
if prest > minimo:
    print(f'Devido a prestação mensal ser de R${prest:.2f} e o seu salário mensal, ser {salário:.2f} excede em muito ao seu atual custo de vida...')
    print('Devido a isso, o seu empréstimo foi negado.')
elif prest <=minimo:
    print(f'A porcetangem a ser paga da prestação é de R${prest:.0f}, e o seu salário mensal é de {salário}.')
    print('O seu empréstimo será aprovado')
elif prest ==30%salário:
    print(f'O seu empréstimo não excede o valor mínimo para requerimento de empréstimo, mas irá pegar uma porcentagem muito alta de seu salário atual.')

sleep(1)

print('Para mais informações, entrar no nosso site: https://www.crefisa.com.br/para-voce/emprestimo-pessoal/')


