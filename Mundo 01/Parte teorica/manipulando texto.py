#cadeia de texto
#'curso em vídeo' #uma cadeia de caracteres com aspas simples
frase= 'Curso em Vídeo Python' #opython usa micro-espaços para armazenar na memória do pc para armazenar essa informações
#cada um desses espaços recebendo um número de índices utilizando indices, incluindo os espaços entre a variavel
#fatiamento em python
#colchete = lista
frase[9:21] #vai ir na frase para pegar o índice 9 até o número antecessor, assim como excel ao selecionar uma lista
#os índices começam do 0 e vai até o número necessário para completar o string
#fatiamento de string, o último valor não entra na string, apenas o seu antecessor
frase[9:21:2] # vai ir pulando o fatiamento de 2 em 2
frase[:5] #quando o início é omitido, começará do índice 0.
frase[15:] #quando o final é omitido, ele irá até o caractere final da string
frase[9::3] #vai do 9 até o final, só que pulando de 3 em 3 caracteres
