n = input('digite algo: ')
print('o tipo primitivo é', type(n))
print('só tem letras?', n.isalpha()) #n é letra?
print('é um número?', n.isnumeric())  #n é numerico?
print('possui apenas espaços?', n.isspace()) #só tem espaço?
print('está em letras maiúsculas?', n.isupper()) #está somente com letras maiúsculas?
print('possui letras e números?'),n.isalnum() #n é alfa númerico?
print('não possuí acentos?', n.isascii())
print('possui apenas números decimais?',n.isdecimal())



