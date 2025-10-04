largura_da_parede= float(input('Em metros, qual é a largura da parede? '))
altura_da_parede= float(input('Em metros, qual é a altura da sua parede? '))
area= largura_da_parede*altura_da_parede
litro_de_tinta= area/2
um_litro_de_tinta='um litro de tinta pinta uma área de 2m²'
print(f'calculando a área das dimensões de sua parede, {largura_da_parede} X {altura_da_parede}, você tem {area:.2f}m².')
print(f'Sabendo que {um_litro_de_tinta}, para pintar a sua parede serão necessários {litro_de_tinta:.2f} litros de tinta.')

