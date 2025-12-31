#n = cont = 0
n = s = 0

while True:
    n = int(input('Inserir um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')



# Gerando número com o flag sendo somado:
'''while n != 999:
    n = int(input('Inserir um número: '))
    s += n
    # cont += 1
s -= 999 #Gambiarra para evitar de somar o valor do flag.
print(f'A soma vale {s}.')'''

