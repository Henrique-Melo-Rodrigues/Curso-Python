total_gasto =  menor_preço = produtos_caros = cont = 0
mais_barato = ''
print('-'*30)
print('LOJA SUPER BARATÃO')

while True:
    produto = str(input('Nome do produto: ')).capitalize().strip()
    preço = float(input('Valor do produto: R$'))
    cont += 1
    total_gasto += preço
    if preço > 1000:
        produtos_caros += 1

    if cont == 1 or preço < menor_preço:
        menor_preço = preço
        mais_barato = produto
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        print('-'*30)
    if opção == 'N':
        print('') #dando um espaçamento.
        break
print('{:-^40}'.format('COMPRAS FINALIZADAS '))
print(f'O total da compra foi: R${total_gasto:.2f}.')
print(f'Temos {produtos_caros} produto(s) custando mais que R$1000,00.')
print(f'O produto mais barato foi o(a) {mais_barato} , custando R${menor_preço}')
