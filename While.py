litri_benzina = 10
while litri_benzina > 0:
    print("accelaram")
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print("mai avem: ", litri_benzina, "litri de benzina")
        print('se aprinde becul rosu')
print('stop! nu mai avem benzina')