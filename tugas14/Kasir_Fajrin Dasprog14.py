#NAMA : MUHAMMAD FAJRIN TSINAN F
#NIM : 20230040086
#SESI  14 DASAR PEMOGRAMAN


barang = input("masukan nama barang :")
harga = int(input("masukan harga :"))
jumlah_barang = int(input("masukan jumlah barang :"))

text = f'''=== Nota Pembelian ===
barang : {barang}
harga : {harga}
jumlah_barang : {jumlah_barang}
total : {harga * jumlah_barang}
'''
file = open('nota.txt', 'a')
file.write(text)
file.close
