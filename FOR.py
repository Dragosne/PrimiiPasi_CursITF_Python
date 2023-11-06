#dalmatieni
#
# for i in range (1, 102, 1):
#     print(f'Dalmatianul cu nr {i}')
#
numere = [3, 7, 10, 20, 30]
# parcurgere lista cu for prin index

# for i in range (0, len(numere)):
#     print(f'indexul curent este: {i}', f'iar numarul curent este: {numere[i]}')

# for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s = s + numar
    print(f'suma este {s}')