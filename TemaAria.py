import math #pentru radical trebuie importat modulul math
print('Se calculeaza Aria si Lungimea cercului!'.upper())
print('=======================================')
R = float(input('Introduceti Raza cercului in cm: '))
Pi = 3.14

print()
print('Diametrul cercului este: ', round(R * 2, 2), ' cm')
print('Lungimea cercului este: ', round(2 * Pi * R, 2), ' cm') #round (a,2) limiteaza a la 2 zecimale
print('Aria cercului este: ', round(Pi * R ** 2, 2), ' cmp')
print()

print('SE CALCULEAZA ARIA SI PERIMETRUL UNUI DREPTUNGHI')
print('=======================================')
print()

L = float(input('Introduceti Lungimea (L) in cm: '))
l = float(input('Introduceti latimea (l) in cm: '))

D = (L ** 2) + (l ** 2)

print('Diagoala Dreptunghiului este: ', round(math.sqrt(D), 2), ' cm')
print('Perimetrul Dreptunghiului este: ', round(2 * (L + l), 2), ' cm')
print('Aria Dreptunghiului este: ', round(L * l, 2), ' cmp')
