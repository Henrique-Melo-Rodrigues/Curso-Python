'''Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

from time import sleep

print('-'*20)
sleep(1)
print('Analisando triângulos')
sleep(1)
l1 = float(input('Inserir lado do triângulo: '))
l2 = float(input('Inserir outro lado do triângulo: '))
l3 = float(input('Inserir o último lado do triângulo: '))

print('É possível formar um triângulo com estes números?')
# É triângulo?
if (l1 + l2) > l3 and (l2 + l3) > l1 and l1 + l3 > l2:
    print("Sim, é possível gerar um triângulo.")

    # Condições:
    if (l1 == l2 and l1 != l3) or\
        (l2 == l3 and l2 != l1) or\
            (l1 == l3 and l1 != l2):
        print('É um triângulo Isóceles.')

    elif l1 == l2 and l1 == l3:
        print('É um triângulo equilátero.')

    else:
        print('Triâgulo com todos os lados diferentes (Triângulo escaleno).')

else:
    print('Não é possível gerar um triângulo...')

print('-' * 20)
