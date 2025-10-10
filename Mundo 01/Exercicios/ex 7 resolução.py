n1= float(input('Primeira nota do aluno: ')) #float porque a nota pode ser quebrada
n2= float(input('Segunda nota do aluno: '))
m= (n1+n2)/2 #Se não tiver ordem de precedência, dará um valor errôneo!
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1,n2,m)) #Depois do ponto flutuante, coloque um digito.

