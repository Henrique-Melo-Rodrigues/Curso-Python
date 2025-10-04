from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
print(f'Dentre os números {n1}, {n2} e {n3}:')
# if n1 >= n2 >= n3: # Forma errada de se fazer
#Forma corrigida:
sleep(2)
#Verificando quem é menor:
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#verificando quem é menor:
maior = n1
if n2>n1 and n2 > n3:
    maior = n2
    if n3 > n1 and n3 > n2:
        maior = n3
print(f'O menor número é {menor}.') #teste do menor valor
print(f'O maior número é {maior}.') #Teste do maior valor


