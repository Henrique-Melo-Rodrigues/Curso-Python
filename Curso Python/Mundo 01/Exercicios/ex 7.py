

conceitos={'mb':10,'b':8,'r':6,'i':4,'na':0}

nome=str(input('Nome do Aluno: '))
rm=str(input('Rm do aluno: '))
m=conceitos[input('nota em matemática: ').lower()]
p=conceitos[input('nota em português: ').lower()]
s=conceitos[input('nota em sociologia: ').lower()]
e=conceitos[input('nota em ética: ').lower()]
eamt=conceitos[input('nota em eamt: ').lower()]
eacn=conceitos[input('nota em eacn: ').lower()]
oet=conceitos[input('nota em oet: ').lower()]
rh=conceitos[input('nota em orh: ').lower()]
tcc=conceitos[input('nota em pdtcc: ').lower()]
tial=conceitos[input('nota em tial: ').lower()]
média=(m+p+s+e+eamt+eacn+oet+rh+tcc+tial)//10 #calcuar média inteira
print('O(a) aluno(a) {}, do RM: {},\n teve a nota média do primeiro bimestre de {}'.format(nome,rm,média))
#correção do chat gpt:
#O erro está acontecendo porque você está digitando,
# por exemplo, mb no input() e o Python entende isso como uma string.
# Mas depois você tenta somar essa string com inteiros
# (como m + p + s + ...), o que dá erro, pois não se pode somar strings com números diretamente.

