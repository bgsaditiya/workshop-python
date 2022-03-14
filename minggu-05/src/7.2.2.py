#Jika Anda memiliki object x, Anda dapat melihat representasi 
#string JSON dengan sebaris kode sederhana:
import json
x = [1, 'simple', 'list']
json.dumps(x)

#Varian lain dari dumps()fungsi, yang disebut dump(), hanya 
#membuat serial objek ke file teks . Jadi jika objek ffile teks
#dibuka untuk ditulis, kita bisa melakukan ini:
json.dump(x, f)

#Untuk memecahkan kode objek lagi, jika fadalah objek file teks 
#yang telah dibuka untuk dibaca:
x = json.load(f)