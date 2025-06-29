"""
Semua sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial : Langkah Berurutan
2. Percabangan : Langkah Melompat Jika Kondisi Terpenuhi
3. Perulangan : Mengulang Langkah Yang Sama Berkali-kali Selama / Sampai Kondisi Terpenuhi
"""


#Sekuensial
print('Ibu berkata, "Pergi ke toko"') #Model Penulisan Kode 1
print("Ibu berkata, \"Pergi ke toko\"") #Model Penulisan Kode 2

print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko ?"')

print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')

print("Maka Budi berangkat ke toko")

print("Dan mulai berbelanja")

print("\n\n\n")
###########################################################################
#Tugas 1
print('Ibu berkata, "Beli 1 botol susu"')
print('Ibu berkata, "Jika ada telur, beli juga 6 butir telur"')
print('Anak menjawab, "OK"')
print("Anak berangkat ke toko")

ada_susu = True
print('Anak bertanya, "Apakah ada Susu?"')
if ada_susu :
    print('Penjaga toko menjawab, "Ada, harganya 5000 untuk 1 botol"')
    print("Anak mengecek harganya, cukup")
    print('Anak berkata, "Apakah ada telur?"')
    ada_telur = False
    if ada_telur :
        print('Penjaga toko menjawab, "Ada telurnya"')
        print("Anak membeli 1 botol susu dan 6 butir telur")
    else:
        print('Penjaga toko menjawab, "Maaf, telurnya habis"')
        print("Anak membeli 1 botol susu saja")
else:
    print('Penjaga toko menjawab, "Tidak ada susu"')
    print("Anak tidak jadi membeli susu")

print("Anak pulang kerumah")

if ada_susu:
    print("Anak menyerahkan hasil belanjanya kepada Ibu")
else:
    print('Anak berkata, "Susunya tidak ada"')


