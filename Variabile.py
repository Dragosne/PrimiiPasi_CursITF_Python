# variabila = zona din memoria unui calculator care tine date
# variabila = o cutiuta in care punem valori

# am declarat si initializat variabilele marca si model
# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica

marca_masina = 'Volvo'
model_masina = 'XC 60'

# loosly type - nu trebuie sa sa specificam tipurile de variabile

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este Modelul: {model_masina}')

# suprascriere - overright
model_masina = 'XC 60 Facelift'
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este Modelul: {model_masina}')

name = 'Georgel'
prenume = 'Pasarel'
varsta  = 34
print(f'{prenume} {name} si are varsta de: {varsta}')