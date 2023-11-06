x = 0
y = 0
z = 0
numere = [33, 43, 33, 3, 3, 7, 5, 89, 90, 32, 34, 37, 24, 0]
print('Sirul contine: ', len(numere), ' numere')
print('Numerele din lista sunt: ', numere)
print()
print('Cautam Valorile 3 si 4 in sir'.upper())
print()
for numar in numere:
    if numar == 3:
        x = x + 1
    if numar == 4:
        y = y + 1
    if numar != 3 and numar != 4:
        z = z + 1
if x > 0:
    print('Cifra 3 apare de:  ', x, ' ori')
else:
    print('Cifra 3 nu exista in sir')
if y > 0:
    print('Cifra 4 apare de:  ', y, ' ori')
else:
    print('Cifra 4 nu exista in sir')
print('In afara cifrelor 3 si 4 ma sunt: ', z, ' valori in sir')