real= float(input('Quantos reais você tem no banco? R$'))
dolar_hoje=5.64
conversao_real_dolar=real/dolar_hoje
print(f'Convertendo o que você tem na carteira, R${real:.2f}, você poderia comprar Us${conversao_real_dolar:.2f}. ')