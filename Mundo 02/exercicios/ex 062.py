a1 = int(input('Inserir o primeiro termo: '))
r = int(input('Inserir a razão da PA: '))
termo = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, end='  →  ')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja ver dessa PA? [digitar 0 irá para a PA] '))
print(f'Fim do programa, foram exibidos um total de {total} termos desta PA.')
