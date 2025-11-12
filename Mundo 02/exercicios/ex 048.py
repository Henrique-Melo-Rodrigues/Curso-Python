# Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três# e que se encontram no intervalo de 1 até 500.
from time import sleep
print('Todos os números ímpares no intervalo de 1 até 500:')
for i in range(1, 501, 2):
    print(i)
    sleep(0.05)
    # Criando uma progressão aritimética:

    if i % 3 == 0:  # se sobrar 0, é um multiplo de 3.
        a1 = 3
        r = 6
        n = ((495 - 3) / 6) + 1
        an = a1 + (n-1) * r
        sn = n / 2 * (a1 + an)
sleep(1)
print(f'A Soma de todos os multiplos ímpares do 3 entre o 1 e 500 é {sn:.0f}')
sleep(0.5)

