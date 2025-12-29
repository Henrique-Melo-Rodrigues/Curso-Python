'''s = 's'
# while s != 'M' or s != 'F': #usar while not in 'MmFf': para facilitar a compreensão
while s not in 'MmFf':
    s = str(input('Escolha um sexo [F/M]: ')).upper().strip()[0]
    if s == 'M' or s == 'F':
        break
    else:
        print('Por favor insira apenas uma das duas opções acima.') #Mantendo o loop até a resposta certa
if s == 'M':
    s = 'masculino'
else:
    s = 'feminino'
print(f'sexo {s} registrado com sucesso.')'''

#correção do gunabara:
sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFF':
    sexo = str(input('Opção inválida, informe com base nas opções [M/F]: '))
print(f'Sexo {sexo} computado com sucesso.')

