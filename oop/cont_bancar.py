class ContBancar:
    #constructorul
    def __init__(self, titularCont, iban):
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
    incercari_activare = 0
    #metode

    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr de incercari {self.incercari_activare}')
        print(f'---------------------------')

    def activareCont(self, pin_utilizator):
        print(f'buna {self.titularCont}')
        if pin_utilizator == self.pin:
            print('card activat')
            self.activ = True
        else:
            print('pin gresit')
            self.incercari_activare = self.incercari_activare + 1 #self.incercari_activare+=1
    def alimentareCont (self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat suma {suma}')
        print(f'Aveti in cont {self.sold}')
    def plataCard(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'ati cheltuit {suma_cheltuita}')
            print(f' aveti in cont {self.sold}')
        else:
            print(f'fonduri insuficiente')
    def salut(self):
        print(f' buna {self.titularCont}')
