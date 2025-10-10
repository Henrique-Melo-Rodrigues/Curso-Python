#Para saber se é possível formar um triângulo:
#"A soma dos comprimentos de dois lados de um triângulo deve ser sempre maior que o comprimento do terceiro lado."
print('-'*20)
print('Analisando triângulos')
print('-'*20)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
print(f'É possível formar um triângulo com as retas {r1}, {r2} e {r3}?')
if r1 + r2 > r3 and r1+r3 > r2 and r2 + r3 > r1:
    verificação = 'Sim. É possível'
else:
    verificação = 'Não é possível'
print(f'{verificação} formar um triângulo.')


