''': Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
quantidade = 0
numeros = []
while True:
    n = (int(input('Inserir um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
        print('-='*40)
        quantidade += 1
    else:
        print(f'O número {n} já foi adicionado... Tente outro número.')
        print('-='*40)
        continue
    escolha = str(input('Deseja continuar? [S/N]').upper().strip()[0])
    while escolha not in 'SsNn':
        print('Opção inválida.')
        print('-='*40)
        escolha = str(input('Deseja continuar? [S/N]').upper().strip()[0])
    if escolha == 'N':
        print('Finalizando programa...')
        break
numeros.sort(reverse=True)
print('-='*40)
print(f'Foram digitados {quantidade} números diferentes e a lista dos números de forma decrescente é {numeros}')
if 5 not in numeros:
    print('E o valor 5 não foi encotrado na lista')
else:
    print('E o valor 5 faz parte da lista!')
