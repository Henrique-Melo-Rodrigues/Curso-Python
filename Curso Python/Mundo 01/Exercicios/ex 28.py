from random import randint #Importando os números aleatórios inteiros
from time import sleep #Importando função para fazer o pc ter um delay na resposta

print('---------Iniciando o sorteio---------') #Deixando o programa mais bonito
print('')#Dando espaço...
sleep(1)
print('O computador escolheu um número entre 0 e 5.\nAcerte que número foi escolhido!') #Contextualização
sleep(1)

n = int(input('Insira um número de 0 a 5: ')) #Escolha do usuário em números inteiros
print('ANALISANDO...')
sleep(2)#esperando 2 segundos

pc = randint(0, 5) #"sorteio dos números

if n == pc : #semrpre usar == para o pc ler como "igual"
    print('Parábens, você acertou o número!')
    print('Sorteio finalizado')
else:
    print('Errou! tente novamente')
    print(f'O número certo era o {pc} e não o {n}!') #número escolhido pelo pc
    print('Reiciando o sorteio...')

print('--_--'*5)





