'''Faça um programa que  leia o ano de nascimento de um jovem e informe, de acordo com a ano:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from time import sleep
from datetime import date

sleep(1)  # delay de 2s
print('-'*10)

sleep(1)  # delay de 1s
print('Seja bem vindo ao serviço de alistamento militar!')
sleep(0.5)  # delay de meio segundo

ano = int(input('em que ano você nasceu? '))
ano_atual = date.today().year
i = ano_atual - ano
sleep(1)

print('-'*10)
print('De acordo com a sua idade...')
sleep(2)

if i > 18:
    saldo = i - 18
    print(f'Você tem {i} anos e já passou da idade de se alistar há {saldo} anos.')
    print(f'O ano em que você se alistou ou deveria se alistar foi em: {ano_atual - saldo}.')
    sleep(1)

    print('''Você já se alistou?
        [ 1 ] sim
        [ 2 ] não''')  # Fazendo uma segunda variação
    resposta = int(input('Inserir resposta: '))
    if resposta == 1:
        print('Processando...')
        sleep(1)
        print('''Tudo em ordem no seu alistamento militar.
Tenha uma boa tarde!''')  # Print em duas linhas usando 3 vezes a aspas simples

    elif resposta == 2:
        print('Processando...')
        sleep(1)
        print('''Você precisa se apresentar em um orgão gorvenamental.
caso contrário, será multado.
para mais informações, acessar: https://www.gov.br/defesa/pt-br/assuntos/servico-militar/perguntas-frequentes-servico-militar''')
    else:
        print('''Por favor responda conforme solicitado:
[ 1 ] para 'sim'
[ 2 ] para 'não' ''')

elif i < 18:
    saldo = 18 - i
    print('Processando...')
    sleep(1)
    print(f'''Você têm {i} anos e ainda faltam {saldo} ano(s) para você se alistar.
Você irá se alistar em {saldo + ano_atual}.
fique atento ao cronograma e documentação para o alistamento militar!
para mais informações, acessar: https://alistamento.eb.mil.br/alistamento''')

elif i == 18:
    print('Processando...')
    sleep(1)
    print(f'''Agora que você tem {i} anos, está na hora de se alistar!
Você já se alistou?
[ Sim ]
[ Não ]''')

    variavel = str(input('Inserir resposta: ')).strip().lower()
    if variavel == 'sim' or 's':
        sleep(1)
        print('''Ótimo. o local para o alistamento militar já está disponível.
Acesse o site: https://alistamento.eb.mil.br/alistamento
para mais informações!''')
    elif variavel == 'não' or 'nao' or 'n':
        sleep(1)
        print('''Busque um poupa tempo ou acesse o site  https://alistamento.eb.mil.br/alistamento
para a realização do alistamento militar.''')
    else:
        print('''Por favor preencha o formulário escrevendo 'sim' ou 'não'. ''')
