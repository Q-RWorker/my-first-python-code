print('Tipe data skalar => Tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe data list/daftar/array')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

print('\nSapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nSapa anak semua')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak : Cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}!')