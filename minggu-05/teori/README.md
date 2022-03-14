# Rangkuman Pertemuan 5
## 7. Input dan output
---
Pada bab 7 ini akan membahas tentang beberapa kemungkinan cara untuk menampilakn output dari sebuah program. beberapa diantaranya data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau output yang berupa file untuk digunakan dimasa mendatang.

## 7.1. Pemformatan Keluaran yang Lebih Menarik
---
Dari pertemuan-pertemuan sebelumnya dapat diketahui sejauh ini ada 2 cara untuk menampilkan output yaitu dengan `pernyataan ekspresi` dan fungsi `print()`. Cara ketiga dengan menggunakan `write()` yang berarti akses untuk menulis file, jika sudah ada maka file akan di replace dan diganti dengan yang baru ditulis.

Menggunakan f-string, teknik ini memperbaiki metode format agar lebih mudah dan efisien digunakan.
```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

Style pemformatan yang baru secara default memanggil metode `__format__()` dari objek untuk ditampilkan. Jika kita hanya ingin menampilkan output dari `str()` atau `repr()`, kita bisa menggunakan flag konversi `!s` atau `!r` dengan format `'{0!s} {0!r}'.format(Data())`.
```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

Fungsi str() untuk mengembalikan representasi nilai yang dapat dibaca manusia, sedangkan repr()untuk menghasilkan representasi yang dapat dibaca oleh interpreter. Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi yang berbeda.

Contoh :
```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

## 7.1.1. Literal String Terformat
---
f-string atau literal string yang diformat menyediakan cara untuk memformat string menggunakan sintaks minimal. `(diperkenalkan dengan Python 3.6)`. Keterbacaan kode tinggi dan karena itu umumnya cara yang disukai untuk memformat literal string. 'f' atau 'F' digunakan sebagai awalan dan {} digunakan sebagai placeholder. Tidak seperti `.format()`, f-string tidak mengizinkan tanda kurung kosong {}. Ekspresi F-string dievaluasi pada waktu proses.

F-string lebih cepat daripada dua mekanisme pemformatan string yang paling umum digunakan, `% - formatting` dan `.format()`. Contoh berikut membulatkan pi ke tiga tempat setelah desimal:
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
Melewati bilangan bulat setelah ':'akan menyebabkan bidang itu menjadi jumlah karakter minimum. Ini berguna untuk membuat kolom berbaris.
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. `!a` berlaku `ascii()`, `!s` berlaku `str()`, dan `!r` berlaku `repr()`:
```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

## 7.1.2. Metode String format()
---
Berikut penggunaan dasar metode `str.format()`:
```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dan karakter di dalamnya (disebut fields format) diganti dengan objek yang diteruskan ke metode `str.format()`. Angka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam metode `str.format()`.
```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

Jika argumen kata kunci keyword argument digunakan dalam metode str.format(), nilainya dirujuk dengan menggunakan nama argumen.
```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Argumen posisi dan kata kunci dapat dikombinasikan secara bergantian:
```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

Jika kita memiliki string format yang sangat panjang yang tidak ingin dipisahkan, alangkah baiknya jika kita bisa mereferensikan variabel yang akan diformat berdasarkan nama alih-alih berdasarkan posisi. Ini dapat dilakukan hanya dengan melewatkan dict dan menggunakan tanda kurung siku '[]' untuk mengakses kunci dari dict
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Ini juga bisa dilakukan dengan memberikan tabel sebagai argumen kata kunci keyword argument dengan notasi '**'
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Contoh, baris-baris berikut menghasilkan kumpulan kolom yang disejajarkan rapi memberikan bilangan bulat dan kotak dan kubusnya:
```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

## 7.1.3. Pemformatan String Manual
---
str.rjust (): Mengembalikan string yang diratakan ke kanan dalam string dengan panjang (lebar). Padding dilakukan dengan menggunakan fillchar. Fillchar default adalah ruang ASCII. String asli dikembalikan jika lebarnya kurang dari atau sama dengan len (s)

Contoh tabel kotak dan kubus yang sama, yang diformat secara manual:
```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Terdapat metode serupa `str.ljust()` dan `str.center()`. Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda, tetapi itu biasanya lebih baik daripada alternatif, yang akan berbohong tentang nilai.

Metode lain `zfill()` metode ini mengisi string dengan sejumlah nilai 0 di awal
```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

## 7.1.4. Pemformatan string lama
---
Operator % (modulo) juga dapat digunakan untuk pemformatan string. Diberikan 'string' % values, instansiasi dari % in string diganti dengan nol atau elemen yang lebih dari values. Operasi ini umumnya dikenal sebagai interpolasi string. Sebagai contoh:
```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

## 7.2. Membaca dan Menulis Berkas
---
Fungsi open() digunakan untuk membuka file dan mengembalikannya berupa objek file dari file yang bersangkutan
```python
>>> f = open('workfile', 'w')
```

Penjelasan :
Argumen pertama merupakan string nama dari file. Argumen kedua berisi mode (opsional) – mode saat membuka file, jika tidak ditentukan defaultnya adalah `'r'` (read).

Untuk mengetahui mode apa saja yang tersedia bisa dilihat di tabel berikut:
| Mode | Keterangan |
| :--: | :--------: |
| `'r'` | Membuka file untuk dibaca (default) |
| `'w'` | Membuka file untuk ditulis. Pada mode ini akan dibuat baris baru jika file masih kosong. Sedangkan jika file tidak kosong maka akan menimpa ke teks yang sudah ada |
| `'x'` | Membuka file untuk pembuatan eksklusif. Jika file sudah ada, maka operasi akan gagal.|
| `'a'` | Membuka file untuk ditambahkan (append) pada akhir file tanpa menimpanya. Jika filenya belum ada akan membuat file baru |
| `'t'` | Membuka file dalam mode teks |
| `'b'` | Membuka file dalam mode biner |
| `'+'` | Membuka file untuk diperbarui (membaca dan menulis) |

Praktik yang baik dengan menggunakan `with` ketika berhubungan dengan objek file.
Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika suatu pengecualian muncul di beberapa titik. Menggunakan with juga jauh lebih pendek daripada penulisan yang setara try-blok finally
```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

Apabila tidak menggunakan kata kunci with, maka harus memanggil f.close() untuk menutup file dan membebaskan sumber daya sistem yang digunakan secara langsung.

`Catatan :  Memanggil f.write() tanpa menggunakan kata kunci with atau memanggil f.close() dapat menyebabkan argumen-argumen dari f.write() tidak dituliskan ke dalam disk secara utuh, meskipun program berhenti dengan sukses.`

Setelah menggunakan `with` ata dengan `f.close()`, kita tidak bisa menggunakan kembali file tersebut.
```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

## 7.2.1. Metode Objek Berkas
---
Objek file adalah variabel objek yang menampung isi file. Kita bisa melakukan pemrosesan file berkatnya. Nama file bisa kita isi langsung apabila file-nya terletak dalam satu direktori dengan skrip python. Namun, apabila terletak di direktori yang berbeda, maka kita harus memberikan alamat path file-nya.

Membaca teks file dengan menggunakan method `f.read(size)`. method ini membaca sejumlah kuantitas data dan mengembalikannya dalam bentuk string atau dalam bentuk binner. size merupakan argumen untuk menentukan ukuran yang ingin kita baca. Ketika size kosong atau bernilai negatif maka seluruh isi file akan dibaca. Method `f.read()` hanya dapat dieksekusi sekali, artinya hanya dapat digunakan sekali saja. Pada eksekusi kedua method `f.read()` akan mengembalikan nilai string kosong `('')`.
```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

Method `f.readlines()` membaca isi file per baris dan akan mengembalikan nilai berupa list. Seberapa banyak baris yang akan ditampilkan tergantung pada jumlah argumen pada method tersebut. Contoh bentuk argumen `f.readlines(5)`.
```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the fil
```

`f.write(string)` menulis konten string ke berkas, mengembalikan jumlah karakter yang ditulis.
```python
>>> f.write('This is a test\n')
15
```

Jenis objek lain perlu dikonversi -- baik menjadi string (dalam mode teks) atau objek byte (dalam mode biner) -- sebelum menulisnya.
```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

## 7.2.2. Menyimpan data terstruktur dengan json
---
Jika kita memiliki objek Python, kita dapat mengubahnya menjadi string JSON dengan menggunakan metode json.dumps().

Contoh konversi python ke json : 
```python
import json

# Python object (dict):
x = {
  "nama": "Bagas",
  "usia": 30,
  "kota": "Yogyakarta"
}
# Konvert menjadi JSON:
y = json.dumps(x)

print(y)
```

Varian lain dari fungsi `dumps()`, disebut `dump()`, dengan mudah membuat serialisasi objek menjadi `:term:` text file. Jadi jika `f` adalah objek text file, kita dapat melakukan ini:
```python
json.dump(x, f)
```

Kemudian untuk membaca file json maka kita gunakan perintah berikut :
```python
import json

with open('orang.json') as f:
  
  # Method untuk membaca file json
  data = json.load(f)

print(data)
```

