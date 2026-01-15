# () --> Tupla; [] --> Lista; {} --> Dicionário.
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis
# lanche[1] = 'Refrigerante'
#'tuple' object does not support item assignment --> tuple não pode receber itens atribuidos
# print(lanche)

'''for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} e na posição {pos}')'''

'''for cont in range(0, len(lanche)):
    print(lanche[cont])'''

'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')'''


print(sorted(lanche)) #Coloca em ordem com o formato de lista
