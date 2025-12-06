# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A media de idade do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
soma = 0
maior = 0
menor = 0
mulher_nova = 0
nome_velho = ''
idade_homem_velho = 0
for i in range(1, 5):
    print('-'*4, f'{i}° Pessoa', '-'*4)
    sexo = str(input('sexo [M/F]: ')).lower().strip()
    nome = str(input('Nome: ')).lower().strip()
    idade = int(input('idade: '))
    soma += idade
    if i == 1 and sexo in'Mm, ':
        nome_velho = nome
        idade_homem_velho = idade
        if sexo in 'Mm' and idade > idade_homem_velho:
            idade_homem_velho = idade
            nome_velho = nome
    if sexo == 'f' and idade <20:
        mulher_nova += 1
média = (soma / 4)
print(f'''A média de idade do grupo é de {média} anos.
O homem mais velho desta lista é {nome_velho} e tem {idade_homem_velho} anos
e há {mulher_nova} mulhere(s) abaixo dos 20 anos.''')
