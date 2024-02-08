from time import sleep
contador = int(10)
print('incio da contagem')

while (contador >= 1):
    sleep(0)
    print(contador)
    contador -= 1
    if (contador == 0):
        print('Foguete lançado')