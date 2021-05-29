class Bola:
    cor = 'unknown'
    circunferencia = 0
    material = 'unknown'

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        troca = str(input(f'Deseja trocar  cor {self.cor}? [s/n]')).upper()
        if troca == 'S':
            nova_cor = str(input('Nova cor:'))
            self.cor = nova_cor
        else:
            print(f'A continuará sendo {self.cor}')

    def mostraCor(self):
        print(f'A cor atual é {self.cor}.')

def main():

    Bola01 = Bola('Preto', 10, 'plástico')

    while True:
        Bola01.mostraCor()
        Bola01.trocaCor()

        escolha = str(input('Deseja continuar?[s/n]')).upper()
        if escolha == 'N':
            break
    Bola01.mostraCor()

main()
        
