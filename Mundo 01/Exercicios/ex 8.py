d=float(input('Uma distância em metros: '))
km=d/1000 #m para km há uma distância de três zeros (km,hm,dam,m,dm,cm,mm)
hm=d/100 #m para hm, muda 2 zeros à esquerda
dam=d/10 #m para dam há uma distância de um zero à esquerda
m=d*1 #metro convertido para metro é o mesmo que multiplicar por 1
dm=d*10 #m para dm, acrescentar um zero à direita
cm=d*100 #acrescentar 2 zeros à direita
mm=d*1000 #três zeros acrescentados à direita
print('{}M convertido em Km é igual a {}Km.'.format(d,km))
print('{}M, se covertido em hecâmetro é igual a {}Hm.'.format(d,hm))
print('Já se {}M for convertido em decâmetro, seu valor será {}Dm.'.format(d,dam))
print('Em decimetros: {:.0f}Dm.'.format(dm)) #sem casas decimais em conversões menores que o metro.
print('{}m convertido em centímetros ={:.0f}Cm.'.format(d,cm))
print('Por fim, se estiver convertendo {}M em milimetros\nele terá o valor de {:.0f}Mm.'.format(d,mm))


