<h1>Rangkuman Pertemuan 3</h1>
<h2>5.1 Lists</h2>

Tipe data daftar memiliki beberapa metode lagi. Berikut adalah semua metode objek daftar:

* list.append( x )

<dd>Tambahkan item ke akhir list. Setara dengan .a[len(a):] = [x]</dd></br>

* list.append( x )
<dd>Tambahkan item ke akhir daftar. Setara dengan .a[len(a):] = [x]</dd></br>

* list.extend( dapat diubah )
<dd>Perluas daftar dengan menambahkan semua item dari iterable. Setara dengan .a[len(a):] = iterable</dd></br>

* list.insert( saya , x )
<dd>Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya, jadi disisipkan di bagian depan daftar, dan sama dengan .a.insert(0, x)a.insert(len(a), x)a.append(x)</dd></br>

* list.remove( x )
<dd>Hapus item pertama dari daftar yang nilainya sama dengan x . Ini menimbulkan ValueErrorjika tidak ada item seperti itu.</dd></br>

* list.pop( [ saya ] )
<dd>Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop()hapus dan kembalikan item terakhir dalam daftar. (Kurung siku di sekitar i dalam tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)</dd></br>

* list.clear( )
<dd>Hapus semua item dari daftar. Setara dengan .del a[:]</dd></br>

* list.index( x [ , mulai [ , akhir ] ] )
<dd>Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a ValueErrorjika tidak ada item seperti itu.</dd></br>

<dd>Argumen opsional mulai dan akhir ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.</dd></br>

* list.count( x )
<dd>Kembalikan berapa kali x muncul dalam daftar.</dd></br>

* list.sort( * , kunci = Tidak ada , terbalik = Salah )
<dd>Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan, lihat sorted()penjelasannya).</dd></br>

* list.reverse( )
<dd>Balikkan elemen daftar di tempatnya.</dd></br>

* list.copy( )
<dd>Kembalikan salinan daftar yang dangkal. Setara dengan a[:].</dd></br>

Hal lain yang perlu diperhatikan adalah tidak semua data dapat diurutkan atau dibandingkan. Misalnya, tidak mengurutkan karena bilangan bulat tidak dapat dibandingkan dengan string dan Tidak Ada tidak dapat dibandingkan dengan tipe lain. Juga, ada beberapa tipe yang tidak memiliki relasi pengurutan yang ditentukan. Misalnya, bukan perbandingan yang valid. [None, 'hello', 10]3+4j < 5+7j

***

<h2>5.1.1 Menggunakan Lists sebagai Stack</h2>

Metode lists membuatnya sangat mudah untuk menggunakan lists sebagai stack, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). Untuk menambahkan item ke bagian atas stack, gunakan append(). Untuk mengambil item dari atas stack, gunakan pop()tanpa indeks eksplisit.

***

<h2>5.1.2 Menggunakan Lists sebagai Queue</h2>

Dimungkinkan juga untuk menggunakan lists sebagai queue, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"); namun, lists tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir lists cepat, melakukan sisipan atau muncul dari awal lists lambat (karena semua elemen lain harus digeser satu).

***
<h2>5.1.3. List Comprehensions</h2>

List comprehensions menyediakan cara ringkas untuk membuat lists. Aplikasi umum adalah untuk membuat lists baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat sub urutan dari elemen-elemen yang memenuhi kondisi tertentu.

***

<h2>5.1.4. Nested List Comprehensions</h2>

Ekspresi awal dalam list comprehensions dapat berupa ekspresi arbitrer, termasuk list comprehensions lainnya.

***

<h2>5.2. The del statement</h2>

Ada cara untuk menghapus item dari list yang diberikan indeksnya alih-alih nilainya: del statement. Ini berbeda dari pop() metode yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari list atau menghapus seluruh list (yang kita lakukan sebelumnya dengan menetapkan list kosong ke irisan).

***

<h2>5.3. Tuples and Sequences</h2>

Kami melihat bahwa list dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pengirisan. Mereka adalah dua contoh tipe data sequence. Karena Python adalah bahasa yang berkembang, tipe data sequence lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple.

Meskipun tupel mungkin tampak mirip dengan list, mereka sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuple tidak dapat diubah , dan biasanya berisi sequence elemen heterogen yang diakses melalui pembongkaran atau pengindeksan (atau bahkan dengan atribut dalam kasus bernama tuples). Daftar bisa berubah, dan elemennya biasanya homogen dan diakses dengan mengulangi daftar.

***

<h2>5.4. Sets</h2>

Python juga menyertakan tipe data untuk set . Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.

Kurung kurawal atau set()fungsi dapat digunakan untuk membuat himpunan. Catatan: untuk membuat set kosong Anda harus menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, struktur data yang akan kita bahas di bagian selanjutnya.

***

<h2>5.5. Dictionaries</h2>

Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus. Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci , yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, penetapan irisan, atau metode seperti append()dan extend().

Yang terbaik adalah menganggap kamus sebagai satu set kunci: pasangan nilai, dengan persyaratan bahwa kuncinya unik (dalam satu kamus). Sepasang kurung kurawal membuat kamus kosong: {}. Menempatkan daftar pasangan kunci:nilai yang dipisahkan koma di dalam kurung kurawal menambahkan pasangan kunci:nilai awal ke kamus; ini juga cara kamus ditulis pada output.

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut. Dimungkinkan juga untuk menghapus pasangan key:value dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci tersebut akan terlupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.

Melakukan list(d)di kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, gunakan sorted(d)saja). Untuk memeriksa apakah satu kunci ada dalam kamus, gunakan inkata kunci.

***

<h2>5.6. Looping Techniques</h2>

Saat mengulang melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan items(). Saat mengulang melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan enumerate()

***

<h2>5.7. More on Conditions</h2>

Kondisi yang digunakan dalam whiledan ifpernyataan dapat berisi operator apa pun, bukan hanya perbandingan.

Operator perbandingan indan merupakan tes keanggotaan yang menentukan apakah suatu nilai ada di (atau tidak) dalam wadah. Operator dan membandingkan apakah dua objek benar-benar objek yang sama. Semua operator pembanding memiliki prioritas yang sama, yaitu lebih rendah dari semua operator numerik.not inisis not

Perbandingan dapat dirantai. Misalnya, menguji apakah kurang dari dan apalagi sama dengan .a < b == cabbc

Perbandingan dapat digabungkan menggunakan operator Boolean anddan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; antara mereka, notmemiliki prioritas tertinggi dan orterendah, sehingga setara dengan . Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.A and not B or C(A and (not B)) or C

Operator Boolean anddan oryang disebut operator hubung singkat : argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika Adan Cbenar tetapi Bsalah, tidak mengevaluasi ekspresi . Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah argumen terakhir yang dievaluasi.A and B and CC

***

<h2>5.8. Comparing Sequences and Other Types</h2>

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingannya menggunakan leksikografispemesanan: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu barisan merupakan sub-urutan awal dari yang lain, barisan yang lebih pendek adalah yang lebih kecil (lebih kecil). Urutan leksikografis untuk string menggunakan nomor titik kode Unicode untuk mengurutkan karakter individual.