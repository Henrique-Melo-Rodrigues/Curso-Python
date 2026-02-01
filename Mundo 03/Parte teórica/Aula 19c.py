estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    # brasil.append(estado) --> Resulta em uma lista duplicada apenas do primeiro elemento
    # brasil.append(estado[:]) --> Não pode usar fatiamento em dicionário
    brasil.append(estado.copy())
for estados in brasil:
    for keys, values in estados.items():
        print(f'O campo {keys} tem valor {values}.')

