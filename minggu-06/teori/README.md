# Rangkuman Pertemuan 6

</br>

## 8. Kesalahan errors dan Pengecualian exceptions
---
Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika telah mencoba contohnya, mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: `syntax errors` dan `exceptions`. 

</br>

## 8.1. Kesalahan Sintaksis
---
Kesalahan sintaksis, juga dikenal sebagai kesalahan penguraian parsing, mungkin merupakan jenis keluhan paling umum yang didapatkan saat masih belajar Python:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

Pengurai parser mengulangi baris yang menyinggung dan menampilkan sedikit 'arrow' yang menunjuk pada titik paling awal di baris di mana kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token preceding panah: dalam contoh, kesalahan terdeteksi pada fungsi `print()`, karena titik dua `(':')` hilang sebelum itu. Nama file dan nomor baris dicetak sehingga tahu ke mana harus mencari kalau-kalau masukan berasal dari skrip.

</br>

## 8.2. Pengecualian
---
Bahkan jika suatu pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut exceptions dan tidak fatal tanpa syarat: kita akan belajar cara menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Baris terakhir dari pesan error menunjukkan apa yang terjadi. Pengecualian ada berbagai jenis yang berbeda, dan tipe dicetak sebagai bagian dari pesan: tipe dalam contoh adalah `ZeroDivisionError`, `NameError` dan `TypeError`. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Ini berlaku untuk semua pengecualian bawaan, tetapi tidak harus sama untuk pengecualian yang dibuat pengguna (meskipun ini adalah konvensi yang bermanfaat). Nama pengecualian standar adalah pengidentifikasi bawaan (bukan kata kunci yang dipesan reserved keyword).

</br>

## 8.3. Menangani Pengecualian
---
Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Lihatlah contoh berikut, yang meminta masukan dari pengguna sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menghentikan program (menggunakan Control-C atau apa pun yang didukung sistem operasi); perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan munculnya pengecualian `KeyboardInterrupt`.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pernyataan try berfungsi sebagai berikut.
- Pertama, try clause (pernyataan(-pernyataan) di antara kata kunci try dan except) dieksekusi.
- Jika tidak ada pengecualian terjadi, except clause dilewati dan eksekusi pernyataan :keyword: try selesai.
- Jika pengecualian terjadi selama eksekusi try clause, sisa clause akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci except, except clause dijalankan, dan kemudian eksekusi dilanjutkan setelah blok try/except.
- Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam except clause, itu diteruskan ke pernyataan try luar; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan try mungkin memiliki lebih dari satu except clause, untuk menentukan penangan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Handler hanya menangani pengecualian yang terjadi di try clause yang sesuai, bukan di handler lain dari pernyataan try yang sama. Except clause dapat menyebutkan beberapa pengecualian sebagai tupel dalam kurung, misalnya:

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

Class dalam except clause kompatibel dengan pengecualian jika itu adalah class yang sama atau class dasar daripadanya (tetapi tidak sebaliknya --- except clause yang mencantumkan class turunan tidak kompatibel dengan class dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Perhatikan bahwa jika except clause dibalik (dengan kecuali B terlebih dahulu), itu akan mencetak B, B, B --- pencocokan pertama except clause dipicu.

Semua pengecualian mewarisi dari BaseException, sehingga dapat digunakan untuk berfungsi sebagai wildcard. Gunakan ini dengan sangat hati-hati, karena mudah untuk menutupi kesalahan pemrograman yang sebenarnya dengan cara ini! Itu juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian (memungkinkan penelepon untuk menangani pengecualian juga):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Sebagai alternatif, except clause terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari `sys.exc_info()[1]`.

Pernyataan try kecuali memiliki pilihan `else clause`, `which`, `when present`, harus mengikuti semua `except clauses`. Berguna untuk kode yang harus dijalankan jika try clause tidak memunculkan pengecualian. Sebagai contoh:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan clause else lebih baik daripada menambahkan kode tambahan ke klausa try karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan try ... :keyword: !except.

Ketika pengecualian terjadi, itu mungkin memiliki nilai terkait, juga dikenal sebagai argument pengecualian. Kehadiran dan jenis argumen tergantung pada jenis pengecualian.

except clause dapat menentukan variabel setelah nama dari pengecualian. Variabel terikat ke instance pengecualian dengan argumen yang disimpan di `instance.args.` Untuk kenyamanan, instance pengecualian mendefinisikan `__str__()` sehingga argumen dapat dicetak secara langsung tanpa harus merujuk ke `.args.` Dapat juga membuat instance pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika pengecualian memiliki argumen, argumen itu dicetak sebagai bagian terakhir ('detail') dari pesan untuk pengecualian yang tidak ditangani.

Pengendali pengecualian tidak hanya menangani pengecualian jika terjadi segera di try clause, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam try clasue. Sebagai contoh:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

</br>

## 8.4. Memunculkan Pengecualian
---
Pernyataan `raise` memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi. Sebagai contoh:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu-satunya argumen untuk `raise` menunjukkan pengecualian yang dimunculkan. Ini harus berupa `instance` pengecualian atau kelas pengecualian (class yang berasal dari `Exception`). Jika class pengecualian dikirimkan, itu akan secara implisit diinstansiasi dengan memanggil pembangunnya `constructor` tanpa argumen:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Jika perlu menentukan apakah pengecualian muncul tetapi tidak bermaksud menanganinya, bentuk yang lebih sederhana dari pernyataan `raise` memungkinkan untuk memunculkan kembali pengecualian:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

</br>

## 8.5. Rantai Pengecualian
---
Pernyataan `raise` memungkinkan opsional `from` yang memungkinkan pengecualian rantai. Sebagai contoh:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

Ini bisa berguna saat mengubah pengecualian. Sebagai contoh:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam bagian kecuali atau akhirnya. Ini dapat dinonaktifkan dengan menggunakan `from None` idiom:

```python
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

</br>

## 8.6. Pengecualian yang Ditentukan Pengguna
---
Program dapat memberi nama pengecualian mereka sendiri dengan membuat class pengecualian baru. Pengecualian biasanya berasal dari class `Exception`, baik secara langsung atau tidak langsung.

Exception class dapat didefinisikan yang melakukan apa pun yang dapat dilakukan class lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian.

Sebagian besar pengecualian didefinisikan dengan nama yang diakhiri dengan "Error", mirip dengan penamaan pengecualian standar.

Banyak modul standar menentukan pengecualiannya sendiri untuk melaporkan kesalahan yang mungkin terjadi pada fungsi yang  ditetapkan. Informasi lebih lanjut tentang class disajikan dalam bab tut-class.

</br>

## 8.7. Mendefinisikan Tindakan Pembersihan
---
Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan. Sebagai contoh:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Jika ada klausa `finally`, klausa untuk `finally` akan dijalankan sebagai tugas terakhir sebelum pernyataan untuk `try` selesai. Klausa untuk `finally` dapat berjalan baik atau tidak apabila pernyataan `try` menghasilkan suatu pengecualian. Poin-poin berikut membahas kasus yang lebih kompleks saat pengecualian terjadi:

- Jika pengecualian terjadi selama eksekusi klausa untuk :keyword: `!try`, maka pengecualian tersebut dapat ditangani oleh klausa `except`. Jika pengecualian tidak ditangani oleh klausa `:keyword: !except`, maka pengecualian dimunculkan kembali setelah klausa `finally` dieksekusi.
- Pengecualian dapat terjadi selama pelaksanaan klausa except atau else. Sekali lagi, pengecualian akan muncul kembali setelah klausa finally telah dieksekusi.
- Jika `finally` clause mengeksekusi pernyataan `break`, `continue`, atau `return`, pengecualian tidak dimunculkan kembali.
- Jika pernyataan klausa untuk try mencapai klausa break, continue atau :keyword: `return` maka, pernyataan untuk klausa `finally` akan dieksekusi sebelum `break`, `continue` atau `return` dieksekusi.

Sebagai contoh:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

Contoh lain yang lebih kompleks:
```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang dilihat, klausa `finally` dieksekusi dalam peristiwa apa pun. `TypeError` yang ditimbulkan dengan membagi dua string tidak ditangani oleh klausa `except` dan karenanya kembali muncul setelah klausa finally telah dieksekusi.

Dalam aplikasi dunia nyata, klausa `finally` berguna untuk melepaskan sumber daya eksternal (seperti berkas atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya tersebut berhasil.

</br>

## 8.8. Tindakan Pembersihan yang Sudah Ditentukan
---
Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Berikut contoh, yang mencoba membuka berkas dan mencetak isinya ke layar.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Masalah dengan kode ini adalah bahwa ia membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan `with` memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dieksekusi, file `f` selalu ditutup, bahkan jika ada masalah saat pemrosesan baris-baris. Objek yang, seperti berkas-berkas, memberikan tindakan pembersihan yang telah ditentukan, akan menunjukkan ini dalam dokumentasinya.
