# desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final,
# mostre os 10 primeiros termos dessa progressao.

a1 = int(input('Inserir o primeiro termo: '))
r = int(input('inserir razão da PA: '))
n_termos = 10
an = a1 + (n_termos-1) * r
an = an + 1

for c in range(a1, an, r):
    print(f'{a1} + ({c - 1} - 1) * {r} = {c}')


print('fim')
