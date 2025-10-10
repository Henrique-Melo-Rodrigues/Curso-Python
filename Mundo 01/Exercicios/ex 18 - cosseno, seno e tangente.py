from math import radians, sin, cos, tan
angulo = int (input('Inserir angulo em graus: '))
conversao= radians(angulo)
seno = sin(conversao)
cosseno = cos(conversao)
tangente = tan(conversao)
print(f'O seno de {angulo} é igual a {seno:.2f}')
print(f'Cosseno de {angulo} = {cosseno:.2f}')
print(f'E {angulo} tem a sua tangente igual a  {tangente:.2f}')




