n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
if m >=5:
    print("Parábens, você passou!")
else:
    print('Precisa estudar mais!')
