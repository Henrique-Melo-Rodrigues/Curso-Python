listagem = ('Pão',0.75,
            'Café', 15.5,
            'Frango',10.9,
            'Arroz', 10,
            'Açaí', 23,
            'leite', 5.75)
print('-'*40)
print('{:^40}'.format('Lista de compras'))
print('-'*40)
for list in listagem:
    if type(list) is str:
        print(f'{list:.<30}', end='')
    else:
        print(f'R${list:5.2f}')
print('-'*40)
