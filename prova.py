# Questão 1)
nome = input("me fale seu nome: ")
idade = input("E qual seria sua idade? ")
altura = input("E sua altura qual seria? ")

print(f'Bem vindo {nome}, então você tem {idade} de idade e {altura} de altura')

# Questão 2)
n1 = int(input('Me fale um número: '))
n2 = int(input('Me fale outro número: '))

soma = n1 * n2
print(soma)

# Questão 3)
n1 = float(input('Me fale um número: ')) 

if(n1 % 2 == 0):
    print('Seu número é par')
else:
    print('Seu número é impar')

# Questão 4) 
base = float(input('Qual o valor da base de um retângulo: '))
altura = float(input('Qual o valor da altura de um retângulo: '))

mult = base * altura

print (f'O valor da área do seu retângulo é {mult}')

#Questão 5)
print('Lembrando sua unidade de medida é metros')
medida = float(input('Me fale uma medida: '))
conversao = medida * 100

print(f' sua nova medida será {conversao} cm')

#Questão 6)
n1 = float(input('Me fale um número: '))
n2 = float(input('Me fale outro número: '))
n3 = float(input('Mais um número: '))

if(n1 > n2 and n1 > n3):
    print('O número 1 é maior')
if(n2 > n1 and n2 > n3):
    print('O número 2 é maior')
if(n3 > n1 and n3 > n2):
    print(' O número 3 é maior')

#Questão 7)
from time import sleep 
contador = int(0)
print ('ínicio da contagem - -')
while (contador <= 10):
   sleep(1)
    print(contador)
    contador += 1

# Questão 8)
list = ['laranja', 'verde', 'roxo', 'vermelho', 'azul', 'rosa' ]

print(list)

# Questão 9)
list = ['laranja', 'verde', 'roxo', 'vermelho', 'azul', 'rosa' , 'laranja', 'laranja', 'roxo', 'verde']
consulta = list.count('laranja')
print(consulta)

#Questão 10)

list = ['goiaba', 'maça', 'melância', 'kiwi']

print(list)