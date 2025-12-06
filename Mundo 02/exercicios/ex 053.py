# crie um programa que leia a frase qualquer e diga se ela é um palindromo, desconsiderando os espacos.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # separando em lista
junto = ''.join(palavras)  # elimando espaços
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'Essa frase é um palindromo!')
else:
    print('Essa frase não é um palindromo.')
