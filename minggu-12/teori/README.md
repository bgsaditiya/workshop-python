# Rangkuman Pertemuan 12
</br>

## Jupyter
---
JupyterLab

Instal JupyterLab dengan pip:
```
pip install jupyterlab
```
Setelah terinstal, luncurkan JupyterLab dengan:
```
jupyter-lab
```
Jupyter
Install classic Jupyter Notebook dengan:
```
pip install notebook
```
Untuk menjalankan Jupyter Notebook:
```
jupyter notebook
```
Voilà
Install Voilà with:
```
pip install voila
```

</br>

## Struktur Data
---
Struktur data adalah cara menyimpan dan mengatur data secara terstruktur pada sistem komputer atau database sehingga lebih mudah diakses.

## List
---
```py
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

Tidak semua data dapat diurutkan atau dibandingkan. Misalnya, `[None, 'hello', 10]` tidak mengurutkan karena bilangan bulat tidak dapat dibandingkan dengan string dan None tidak dapat dibandingkan dengan jenis lainnya. Juga, ada beberapa tipe yang tidak memiliki hubungan pengurutan yang ditentukan. Sebagai contoh, `3+4j < 5+7j` bukan perbandingan yang valid.

</br>

## Using Lists as Stacks
---
Metode list membuatnya sangat mudah untuk menggunakan list sebagai stack, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Sebagai contoh:
```py
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

</br>

## Using Lists as Queues
---
Untuk mengimplementasikan queue, gunakan `collections.deque` yang dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Sebagai contoh:
```py
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

</br>

##  List Comprehensions
---
Pemahaman list comprehensions menyediakan cara singkat untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota dari urutan lain atau iterable, atau untuk membuat urutan elemen-elemen yang memenuhi kondisi tertentu.
```py
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

</br>

## Nested List Comprehensions
---
Ekspresi awal dalam pemahaman daftar list comprehension dapat berupa ekspresi acak arbitrary, termasuk pemahaman daftar list comprehension lainnya.

Perhatikan contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar list 3 dari daftar list panjang 4
```py
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
Seperti yang kita lihat di bagian sebelumnya, `listcomp` bersarang dievaluasi dalam konteks for yang mengikutinya, jadi contoh ini setara dengan:
```py
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

</br>

## The del statement
---
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya, bukan nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list. Sebagai contoh:
```py
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

</br>

## Tuples and Sequences
---
Kita melihat bahwa daftar list dan string memiliki banyak properti yang sama, seperti operasi pengindeksan dan pemotongan. Mereka adalah dua contoh tipe data sequence. Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lain: tuple.
```py
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

</br>

## Sets
---
Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Atur objek juga mendukung operasi matematika seperti penyatuan union, persimpangan intersection, perbedaan difference, dan perbedaan simetris.
```py
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

</br>

## Dictionaries
---
Operasi utama pada kamus dictionary adalah menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan kunci key. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan del. Jika menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan. Merupakan kesalahan untuk mengekstraksi nilai menggunakan kunci yang tidak ada.
```py
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

</br>

## Looping Techniques
---
Saat mengulang kamus dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode items().
```py
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

</br>

## More on Conditions
---
Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.

```py
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

</br>

## Comparing Sequences and Other Types
---
Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan lexicographical: pertama dua item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai urutan mana pun habis.
```py
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```