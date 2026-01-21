'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
numbers = []
while True:
    n = int(input('Inserir um número: '))
    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print(f'{n} já existe na lista de números... Não vou adicionar novamente.')
        continue
    opção = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    while opção not in 'SsNn':
        print('Opção inválida.')
        opção = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    if opção in 'Nn':
        break
numbers.sort()
print(f'os números em ordem crescente são: {numbers}')


