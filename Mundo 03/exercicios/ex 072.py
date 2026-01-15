número = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

continuar = True
while continuar:
    n = int(input('Inserir número entre 0 e 20: '))
    if 0 <= n <=20:
        print(f'Você digitou o número {número[n]}. ')
        while True:
            opção = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
            if opção == 'N':
                continuar = False
            break
            print('Resposta inválida. Digite S ou N.')
    else:
        print('Opção inválida')
print('Programa finalizado.')
