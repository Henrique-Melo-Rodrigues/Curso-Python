# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A media de idade do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
soma = 0
maior = 0
menor = 0
mulher_nova = 0
nome_velho = ''
for i in range(1, 5):
    print('-'*4, f'{i}° Pessoa', '-'*4)
    sexo = str(input('sexo: ')).lower()
    nome = str(input('Nome: ')).lower().strip()
    idade = int(input('idade: '))
    if i == 1:
        soma = idade
    else:
        soma = idade + soma
        if sexo == 'feminino' or 'fem':
            mulher_nova += 1
        elif sexo == 'masculino' or 'masc':
            maior = idade
            menor = idade
            nome_velho = nome
            if idade > maior:
                maior = idade
                nome_velho = nome
            if idade < menor:
                menor = idade
média = (soma / 4)
print(f'''A média de idade do grupo é de {média} anos.
O homem mais velho desta lista é {nome_velho}
e há {mulher_nova} mulhere(s) abaixo dos 20 anos.''')
