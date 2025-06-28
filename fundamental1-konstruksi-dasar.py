#Konstruksi dasa Python
#Sequential : Eksekusi Berurutan
print('Hello World!')
print('By Aqsha')
print('Date, 28 June 2025')
print('-' * 10)

#Percabangan : Eksekusi Terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('jalan lain')

#Perulangan
jumlah_anak = 4

for index_anak in range(1,jumlah_anak+1):   #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')