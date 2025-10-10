import math

n = int(input('Insira o ano: '))
bissexto = n % 4 == 0
arg = math.gcd(n, 100)
arg_2 = math.gcd(n, 400)
if n ==  bissexto or arg and arg_2:
    print(f'{n} é um ano bissexto')
else:
    print(f'{n} não é um ano bissexto.')


