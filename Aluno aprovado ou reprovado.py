n1= float(input('Me fale sua primeira nota: '))
n2= float(input('Me fale sua segunda nota: '))
n3= float(input('Me fale sua terceira nota: '))
n4= float(input('Me fale sua quarta nota: '))

media = (n1+n2+n3+n4)/4
print(media)

if (media >= 6):
    print('você está aprovado')
else:
    print('você está reprovado')