piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dau mai tare')
    print('íncep sa fredonez')
print('opresc radioul')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar

nr = 5
if nr % 2 == 0:
    print('numarul este par')
else:
    print('numarul este impar')
if nr > 0:
    print('numarul este pozitiv')
else:
    print('numarul este negativ')

# if else if else
# cum ne saluta robotelul in functie de ora
# daca utilizatorul are peste 18 ani nu poate paria

ora = int(input('íntrodu ora'))
print(ora == 17)