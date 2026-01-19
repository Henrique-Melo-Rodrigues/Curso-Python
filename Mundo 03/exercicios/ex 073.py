from time import sleep

tabela = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia',
          'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians',
          'Vasco da Gama', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport Recife')

print('{:-^40}'.format('Tabela do Brasileirão 2025'))
sleep(1)
for posição in (tabela):
    print(posição)
    sleep(0.125)

print('-='*20 )
print(f'Os cinco primeiros colados são: {tabela[0:5]}')
sleep(0.5)
print('-='*20 )
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
sleep(0.5)
print('-='*20 )
print(f'Times em ordem alfabética: {sorted(tabela)}')
sleep(0.5)
print('-='*20 )
print(f'O Santos acabou o Brasileirão na {tabela.index('Santos') + 1}° colocação')
sleep(0.5)
print('-='*20 )
print('FIM')
print('-='*20 )

