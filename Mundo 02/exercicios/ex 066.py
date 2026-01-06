soma = contador = 0
while True:
    n = int(input('Inserir um número [999 para encerrar o programa]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Foram digitados {contador} números e a soma entre eles foi {soma}.')

