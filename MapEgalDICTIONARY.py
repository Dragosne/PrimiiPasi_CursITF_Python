# Declaram si initializam un dict

list_goala = []
dict_gol = {}

note_elevi = {'Gigel' : 10, 'costel' : 9, 'Ana' : 10}
# adaugam elemente

note_elevi['Sebi'] = 7
print(note_elevi)
print('ce nota a luat gigel?', 'A luat nota: ', note_elevi['Gigel'])
print('ce nota a luat Ana?', 'A luat nota: ', note_elevi.get('Ana'))

# actualizam valori
note_elevi['Costel'] = 10
# aflam dimensiunea
print(len(note_elevi))
# sterg valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai acest elev'))
print(note_elevi)
print(note_elevi.keys())
