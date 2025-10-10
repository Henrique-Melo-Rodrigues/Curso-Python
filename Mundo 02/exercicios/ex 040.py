'''Crie um programa que leia duas notas de um aluno, calcule e mostre a média final.
- Se a média for maior ou igual a 7, exiba uma mensagem de "Aprovado"
- Se a média for entre 5.0 e 6.9, exiba uma mensagem de "Recuperação"
- Se a média for menor que 5.0, exiba uma mensagem de "Reprovado"
'''

from time import sleep

print('-'*40)
sleep(1)
print('     Calculadora de média de notas...        ')
sleep(1)

p = float(input('Inserir nota de português: '))
m = float(input('Inserir nota de matemática: '))

média = (p+m)/2

print(f'A média de notas do aluno foi de {média:.2f}.')

if média >= 7:
    sleep(1)

    print('Aluno aprovado')

elif média == 5 and média <= 6.9:

    sleep(1)
    print('Aluno em recuperação.')

elif média < 5:
    sleep(1)

    print('Aluno reprovado.')


sleep(1)
print('        Fim do cálculo.       ')
print('-'*40)
