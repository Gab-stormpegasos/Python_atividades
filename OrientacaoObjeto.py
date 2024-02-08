class Televisao:

    def __init__(self, canal = 0):
        self.ligada = 'A tv está ligando'

    def canal_valido (self, canais_valor):
        if canais_valor ==2:
            print('Você está na TV globinho')
            return
        elif canais_valor == 4:
            print('Você está na Record')
            return
        elif canais_valor == 9:
            print('Você está no SBT')
            return
        elif canais_valor == 11:
            print('Você estpa na Band')
            return
        elif canais_valor == 13:
            print('Você está na TV Cultura')
            return
        elif canais_valor == 14:
            print('Você está na TV UFG')
            return
        elif canais_valor == 21:
            print('Você está na rede TV')
            return
        else:
            print('O canal digitado está fora , Favor digite um canal valido')
            return
    
TV = Televisao()
print(TV.ligada)
TV.canal_valido(float (input('Digite o canal desejado: ')))