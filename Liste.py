#in python sunt mai simplute
#listele in python pot sa cuprinda elemente de tipuri diferite
#au o dimensiune dinamica
fructe = ['mar', 'portocala', 'banana' , 3 , True]

#aflam lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adugam un alement
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'
print(fructe)

#aflam dimensiunea
print(len(fructe))

# scoatem si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element:', last)
print('lista noua', fructe)

# de cate ori apare un element identic
fructe.append(3)
print(fructe)
print(fructe.count(3))

# extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)