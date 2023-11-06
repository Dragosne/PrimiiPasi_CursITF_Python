# if else if else
# cum ne saluta robotelul in functie de ora
# daca utilizatorul are peste 18 ani nu poate paria

ora = int(input('íntrodu ora'))
if ora < 0:
    print('ora negativa')
elif ora <= 11:
    print('buna dimieata')
elif ora <= 18:
    print('buna ziua')
elif ora <= 21:
    print('buna seara')
elif ora <=24:
    print('noapte buna')
else:
    print('introdu o ora valida')
# cmmd + /