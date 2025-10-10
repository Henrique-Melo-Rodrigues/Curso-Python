frase = 'Curso em Vídeo Python'
frase.split() #Vai pegar na onde tem espaço e criar uma nova ordem de caracteres
#dividindo a palavra 1 da 2 e assim por diante.
#recebendo uma lista nova de toda a cadeia de caracteres
#split vai dividir um string por uma nova lista
#'-'.join(frase) #vai juntar uma string única com ('-'), podendo ser com espaços vazios também (' ')
#para chamar a lista é preciso colocar o nome da variável e para pedir oq vc quer saber
#por exemplo:
frase = 'Curso em vídeo Python'
dividido = frase.split()
print(frase[0]) # vai pegar a primeira lista ou palavra da sua frase
print(len(frase[0])) #vai mostras quantas letras tem nessa primeira sub-lista
