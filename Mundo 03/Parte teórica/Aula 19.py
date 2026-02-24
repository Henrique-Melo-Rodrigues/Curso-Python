pessoas = {
    'Nome': 'Henrique', 'Sexo': 'M', 'Idade': 18
}
pessoas['Peso'] = 61
pessoas['Nome'] = "Henrico"
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos') # Usar aspas dupla
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items()) #Composição de elementos: Gera uma lista com tuplas para cada item no key no dicionário

for keys, values in pessoas.items(): #Utilizar items() ao invés de enumerate()
    print(f'{keys}: {values}')
