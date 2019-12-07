angka1 =int(input('masukkan angka pertama :'))
angka2 =int(input('masukkan angka kedua :'))
print('operator :1. penjumlahan\n 2. pengurangan\n'
'3. perkalian\n 4. pembagian')
pilih=int(input('pilih operator : '))
if pilih == 1:
    tambah = angka1+angka2
    print('hasilnya adalah :',tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print('hasilnya adalah :',kurang)
elif pilih == 3:
    perkalian = angka1*angka2
    print('hasilnya adalah :',perkalian)
elif pilih == 4:
    pembagian = angka1/angka2
    print('hasilnya adalah :',pembagian)
else:
    print('operator yang anda masukkan tidak ada')