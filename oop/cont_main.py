from oop.cont_bancar import ContBancar

cont1 = ContBancar('Dragos', 'RO0002')
cont2 = ContBancar('Laura', 'RO0 3333 002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(5555)
cont2.activareCont(7777)

cont1.alimentareCont(300.5)
cont2.alimentareCont(600)
cont2.alimentareCont(400)

cont1.plataCard(500)
cont1.plataCard(300.5)
cont1.alimentareCont(175.35)

cont2.plataCard(500)
cont2.plataCard(250)


cont1.interogareSold()
cont2.interogareSold()

# tema
# clasa angajat
# nume prenume salariu vechimr
# constructor: nume prenume salariu functie vechime
#metode
# descriere
# marime salariu in functie de vechime
# %actualizare vechime - self.vechime = noua_vechime
# daca are vechime sub 5 ani, marim cu 300, peste 5 ani, 500