#functii pentru TemaCaractere
def numeIntrodus(x):
    print(f'Numele are:', len(x), ' litere')
def numereIntroduse(m, n, o):
    if m > n and m > o:
        print('numarul ', m, ' este cel mai mare')
    elif n > m and n > o:
        print('numarul ', n, ' este cel mai mare')
    elif o > m and o > n:
        print('numarul ', o, ' este cel mai mare')
    else:
        print('numerele sunt egale!'.upper())