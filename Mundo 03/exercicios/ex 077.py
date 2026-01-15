palavra = ('Aprender',
           'Python',
           'Framework',
           'Programacao',
           'Curso em video')
# vogal = 'A', 'E', 'I', 'O', 'U'


for i in palavra:
    print(f'\nNa palavra {i.upper()} temos as vogais: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

