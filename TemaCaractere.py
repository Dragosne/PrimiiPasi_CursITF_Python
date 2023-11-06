from FunctieNume import numeIntrodus
from FunctieNume import numereIntroduse
print('AFLAM CATE CARACTERE ARE NUMELE INTRODUS')
print()
nume = str(input('Introduceti un nume: '))
# print('numele introdus este: ', nume)

numeIntrodus(nume)
print()
print('AFLAM CARE NUMAR ESTE MAI MARE')
print()

print('Introduceti 3 numere intregi pozitive:')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
# print('numerele introduse sunt: ', a, ' ', b, ' ', c)

numereIntroduse(a,b,c)
