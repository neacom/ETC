#Input, Output, Tipe data, Operator, Variable, Statement, Expression dan Komentar

print("Nea")
#print merupakan perintah unuk menampilkan sesuatu ke media output
#kurung adalah prgram yang di jalankan
#tanda petik untuk menandakan string yang

#data yang tersimpan dalam komputer memiliki jenis atau type
#dalam python ada beberapa type data dasar yang sering di gunakan dalam pemrograman
#yaitu:
#Sring: karakter atau text
#Integer: bilangan bulat seperti 7
#Float: bilangan pecahan seperti 7.6
#Boolean: logika benar atau salah yaitu True dan False

#string
# \ mengabakan pindah baris seingga bisa menulis secara lebih dari satu baris namun hanya di anggap sebagai satu baris
# \n untuk berpindah baris
# \t untuk tab
# \\ agari backslash tidak di anggap sebagai escape character
# \' agar ' tidak dianggap sebagai tanda pembuka atau penutup string
# \" agar " tidak dianggap sebagai tanda pembuka atau penutup string
print("Ini \
dua baris tapi dianggap satu baris")
print("ini baris pertama \n baris kedua \n baris ketiga")
print("a\tb\tc")
print("untuk menampilkan backslash menggunakan double backslash \\")
print('untuk menggunakan tanda petik satu tetapi untuk menampilkan yang harus menggunakan tanda petik satu pula maka bisa menggunakan backslash juga seperti berikut it\'s')
print('begitu pula dengan tanda tanda lainnya \!')

#integer
#untuk menampilkan atau memasukkan integer tidak memerlukan tanda petik '/"
print(type("123"))
print(type(123))
#untuk nilai yang berisi koma maka menggunakan tanda titik
#untuk nilai yang memiliki koma maka termasuk pada type data float
print(type(1.3))
#untuk menuliskan exponen juga dapat dalam float
print(3E4)
print(453345E-3)

#boolean
#bolean menyimpan nilai True dan False atau 1 dan 0
print(type(True))

#Operator
print(43+12)
print(34-2)
print(2*3)
print(4/2)
print(2**2)
#modulo / sisa
print(8 % 2)
#integer division
print(6//4)
print(-6//4)