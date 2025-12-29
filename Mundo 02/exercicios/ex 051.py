# desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final,
# mostre os 10 primeiros termos dessa progressao.

a1 = int(input('Inserir o primeiro termo: '))
r = int(input('inserir razão da PA: '))
an = 0

for c in range(1, 11):
    an = a1 + (c - 1) * r
    print(f'{an}',end=' → ')

print('FIM')
