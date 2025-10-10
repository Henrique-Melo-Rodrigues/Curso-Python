from datetime import date
ano = int(input('Que ano você quer análisar? Digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year # vai pegar o ano atual da máquina

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0: #!= diferente
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
