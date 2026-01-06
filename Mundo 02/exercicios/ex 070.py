total_gasto = mais_barato = produtos_caros = 0

print('-'*20)
print('LOJA SUPER BARATÃO')

while True:
    produto = str(input('Nome do produto: ')).capitalize().strip()
    preço = int(input('Valor do produto: R$'))
    total_gasto += preço
    mais_barato = produto
    if produto < mais_barato:
        mais_barato = produto
    if preço > 1000:
        produtos_caros += 1

    opção = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break

print(f'O total da compra foi: R${total_gasto:.2f}.')
print(f'Temos {produtos_caros} custando mais que R$1000,00.')
print(f'O produto mais barato foi a {produto} custando {mais_barato}')
