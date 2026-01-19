'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

minimo = min(valores)
maximo = max(valores)

print(f'Você digitou os valores: {valores}')
print(f'O menor número digitado foi o número {minimo} e apareceu nas posições...',end=' ')
for i,v in enumerate(valores):
    if v == minimo:
        print(i, end=' ')

print(f'\nO maior número digitado foi o número {maximo} e apareceu nas posições...',end=' ')

for i,v in enumerate(valores):
    if v == maximo:
        print(i, end=' ')



