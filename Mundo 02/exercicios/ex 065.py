soma = média = quantidade = maior = menor = 0
r = 'S'.upper().strip()[0]
while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    soma += n
    quantidade +=1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
média = soma / quantidade
print(f'Você digitou {quantidade} números e a média entre eles foi {média:.2f}.')
print(f'o maior valor digitado foi {maior} e o menor {menor}')
print('FIM')
