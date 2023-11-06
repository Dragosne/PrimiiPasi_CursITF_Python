def printGretting():
    print('buna ziua bine ati venit')
def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')
def mediaNr(a, b, c):
    return((a + b + c) / 3)
def piValue():
    return 3.14 # dupa return nu se mai executa nici o linie de cod
# daca numarul este pozitiv returnati true altfel fals
# daca persoana este majora, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


# zona de apelare

printGretting()
printGretting()
printGreetingByName('Dragos', 'Nechifor')
printGreetingByName('Laura', 'Nechifor')
printGreetingByName('Ariana', 'Nechifor')
print(mediaNr(3,4,5))
print (verificareMajor(18))

age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie')
else:
    print('nu ai varsta necesara')
