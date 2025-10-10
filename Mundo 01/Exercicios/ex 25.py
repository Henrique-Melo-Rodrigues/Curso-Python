nome = str(input('Inserir seu nome completo: ')).strip().upper()
sim = 'SILVA' in nome #Procurar o silva em qualquer lugar do nome
print(f'Seu nome tem Silva? {sim}') #Se tiver = true; false