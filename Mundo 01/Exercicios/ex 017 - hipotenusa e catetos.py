import math
ca= float(input('inserir valor do cateto adjacente: '))
co= float(input('inserir valor do cateto oposto: '))
hipotenusa = math.hypot(ca, co)
#hipotenusa= pow(ca,2)+pow(co,2)
print(f'analisando os catetos, é possível saber o valor da hipotenusa: {hipotenusa:.2f}')


