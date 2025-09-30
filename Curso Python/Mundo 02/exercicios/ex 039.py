'''Faça um programa que  leia o ano de nascimento de um jovem e informe, de acordo com a ano:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from time import sleep
from datetime import date

sleep(2)  # delay de 2s
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
    print('Você já passou da idade de se alistar!')
    print('''Você já se alistou?
        [ 1 ] sim
        [ 2 ] não''')  # Fazendo uma segunda variação
    resposta = int(input('Inserir resposta: '))
    if resposta == 1:
        print('Processando...')
        sleep(2)
        print('''Tudo em ordem no seu alistamento militar.
        Tenha uma boa tarde!''')  # Print em duas linhas usando 3 vezes a aspa simples

    elif resposta == 2:
        print('Processando...')
        sleep(2)
        print('''Você precisa se apresentar em um orgão gorvenamental.
    caso contrário, será multado.
    para mais informações, acessar: https://www.gov.br/defesa/pt-br/assuntos/servico-militar/perguntas-frequentes-servico-militar''')
    else:
        print('''Por favor responda conforme solicitado:
        [ 1 ] para 'sim'
        [ 2 ] para 'não' ''')

elif i < 18:
    print('Processando...')
    sleep(2)
    print('''Você ainda vai se alistar.
fique atento ao cronograma e documentação para o alistamento militar!
para mais informações, acessar: https://alistamento.eb.mil.br/alistamento''')

elif i == 18:
    print('Processando...')
    sleep(2)
    print('''Você está no prazo de se alistar!
Você já se alistou?
    [ Sim ]
    [ Não ]''')

    variavel = str(input('Inserir resposta: ')).strip().lower()
    if variavel == 'sim' or 's':
        sleep(2)
        print('''Ótimo. o local para o alistamento militar já está disponível.
        Acesse o site: https://alistamento.eb.mil.br/alistamento
        para mais informações.''')
    elif variavel == 'não' or 'nao' or 'n':
        sleep(2)
        print('''Busque um poupa tempo ou acesse o site  https://alistamento.eb.mil.br/alistamento
        para a realização do alistamento militar.''')
    else:
        print('''Por favor preencha o formulário escrevendo 'sim' ou 'não'. ''')
