# Rangkuman Pertemuan 9
</br>

## 12. Environments dan Paket Virtual
---
</br>

## 12.1. Pengantar
---
Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari pustaka standar. Aplikasi kadang-kadang membutuhkan versi pustaka tertentu, karena aplikasi mungkin mensyaratkan bug tertentu telah diperbaiki atau aplikasi dapat ditulis menggunakan versi usang dari antarmuka pustaka.

Ini berarti tidak mungkin bagi satu instalasi Python untuk memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratannya bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat virtual environment, sebuah struktur direktori mandiri yang berisi instalasi Python untuk versi tertentu dari Python, serta sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan environments virtual yang berbeda. Untuk menyelesaikan contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi A dapat memiliki environments virtual sendiri dengan versi 1.0 yang diinstal sementara aplikasi B memiliki environments virtual lain dengan versi 2.0. Jika aplikasi B membutuhkan pustaka ditingkatkan ke versi 3.0, ini tidak akan mempengaruhi environments aplikasi A.
</br>

## 12.2. Menciptakan Environments Virtual
---
Modul yang digunakan untuk membuat dan mengelola environments virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang kita miliki. Jika memiliki beberapa versi Python di sistem, kita dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang diinginkan.

Untuk membuat environments virtual, tentukan direktori tempat ingin meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori:
```
python3 -m venv tutorial-env
```
Lokasi direktori yang umum dipakai untuk environments virtual adalah `.venv`. Nama ini membuat direktori biasanya tersembunyi di shell dan dengan demikian terpencil sambil memberikan nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrok dengan berkas definisi variabel environments `.env` yang didukung beberapa peralatan.

Di Windows, operasikan:
```
tutorial-env\Scripts\activate.bat
```
(Skrip ini ditulis untuk bash shell. Jika menggunakan csh atau fish shells, ada pilihan skrip `activate.csh` dan `activate.fish` alternatif yang dapat digunakan.)

Mengaktifkan environments virtual akan mengubah prompt shell untuk menunjukkan environments virtual apa yang digunakan, dan memodifikasi environments sehingga menjalankan `python` akan membuat kita mendapatkan versi dan instalasi Python tertentu. Sebagai contoh:
```python
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```
</br>

## 12.3. Mengelola Paket dengan pip
---
Kita dapat menginstal, mengupgrade, dan menghapus paket menggunakan program yang disebut pip. Secara bawaan pip akan menginstal paket dari Python Package Index, https://pypi.org.

`pip` memiliki sejumlah sub-perintah: "install", "uninstall", "freeze", dls.

Kita dapat menginstal versi terbaru dari suatu paket dengan menyebutkan nama suatu paket:
```
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```
Kita juga dapat menginstal versi spesifik suatu paket dengan memberikan nama paket diikuti dengan `==` dan nomor versi:
```
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```
Jika menjalankan kembali perintah ini, pip akan melihat bahwa versi yang diminta sudah diinstal dan tidak melakukan apa-apa. Kita dapat memberikan nomor versi yang berbeda untuk mendapatkan versi itu, atau dapat menjalankan `pip install --upgrade` untuk meningkatkan paket ke versi terbaru:
```
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```
`pip uninstall` diikuti oleh satu atau beberapa nama paket akan menghapus paket-paket dari environments virtual.

`pip show` akan menampilkan informasi tentang paket tertentu:
```
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```
`pip list` akan menampilkan semua paket yang diinstal di environments virtual:
```
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```
`pip freeze` akan menghasilkan daftar yang sama dari paket yang diinstal, tetapi keluarannya menggunakan format yang diharapkan oleh `pip install`. Sebuah konvensi yang umum digunakan adalah meletakkan daftar ini dalam file `requirements.txt`:
```
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
`requirements.txt` kemudian dapat dikirimkan atau commit ke sistem kontrol versi dan dikirim sebagai bagian dari aplikasi. Pengguna kemudian dapat menginstal semua paket yang diperlukan dengan `install -r`:
```
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```
</br>

## Getting started with conda
---
Conda adalah manajer paket dan manajer environments yang kuat yang kita gunakan dengan perintah baris perintah di Anaconda Prompt untuk Windows, atau di jendela terminal untuk macOS atau Linux.
</br>

## Starting conda
---
Windows
- Dari menu Start, cari dan buka "Anaconda Prompt."
Di Windows, semua perintah di bawah ini diketik ke jendela Anaconda Prompt.
</br>

## Managing conda
---
Verifikasi bahwa conda diinstal dan berjalan di sistem dengan mengetik:
```
conda --version
```
Conda menampilkan nomor versi yang telah diinstal. Kita tidak perlu menavigasi ke direktori Anaconda.

Perbarui conda ke versi saat ini. Ketik berikut ini:
```
conda update conda
```
Conda membandingkan versi dan kemudian menampilkan apa yang tersedia untuk diinstal.

Jika versi conda yang lebih baru tersedia, ketik yuntuk memperbarui:
```
Proceed ([y]/n)? y
```
</br>

## Managing environments
---
Conda memungkinkan kita membuat environments terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan environments lain.

Saat mulai menggunakan conda, kita sudah memiliki environments default bernama `base`. Jika tidak ingin memasukkan program ke dalam environments dasar. Buat environments terpisah untuk menjaga program tetap terisolasi satu sama lain.

1. Buat environments baru dan instal paket di dalamnya.
   
   Kita akan memberi nama environment `snowflakes` dan menginstal paket BioPython. Di Anaconda Prompt atau di jendela terminal, ketikkan script berikut ini:
   ```
   conda create --name snowflakes biopython
   ```
   Conda memeriksa untuk melihat paket tambahan ("dependensi") apa yang dibutuhkan BioPython, dan menanyakan apakah kita ingin melanjutkan:
   ```
   Proceed ([y]/n)? y
   ```
   Ketik "y" dan tekan Enter untuk melanjutkan.

2. Untuk menggunakan, atau "mengaktifkan" environments baru, ketik berikut ini:
   - Windows:`conda activate snowflakes`
   - macOS dan Linux:`conda activate snowflakes`
  
    Untuk versi conda sebelum 4.6, ketik:
    - Windows:`activate snowflakes`
    - macOS dan Linux:`source activate snowflakes`

    Sekarang kita berada di environment `snowflakes`, setiap perintah conda yang diketik akan masuk ke environment itu sampai kita menonaktifkannya.

3. Untuk melihat daftar semua environments, ketik:
   ```
   conda info --envs
   ```
   Daftar environments muncul, mirip dengan berikut ini:
   ```
   conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes
    ```
4. Ubah environments kembali ke default (basis): `conda activate`
</br>

## Managing Python
---
Saat membuat environments baru, conda menginstal versi Python yang sama dengan yang kita gunakan saat mengunduh dan menginstal Anaconda. Jika ingin menggunakan versi Python yang berbeda, misalnya Python 3.5, cukup buat environments baru dan tentukan versi Python yang diinginkan.

1. Buat environments baru bernama "snakes" yang berisi Python 3.9:
    ```
    conda create --name snakes python=3.9
    ```
    Ketika conda bertanya apakah ingin melanjutkan, ketik "y" dan tekan Enter.

2. Aktifkan environments baru:
    - Windows:`conda activate snakes`
    - macOS dan Linux:`conda activate snakes`
    
    Untuk versi conda sebelum 4.6, ketik:

    - Jendela:`activate snakes`
    - macOS dan Linux:`source activate snakes`

3. Verifikasi bahwa snakes environment telah ditambahkan dan aktif:
    ```
    conda info --envs
    ```
    Conda menampilkan daftar semua environments dengan tanda bintang (*) setelah nama environments aktif:
    ```
    # conda environments:
    #
    base                     /home/username/anaconda3
    snakes                *  /home/username/anaconda3/envs/snakes
    snowflakes               /home/username/anaconda3/envs/snowflakes
    ```
    Environments aktif juga ditampilkan di depan prompt di (tanda kurung) atau [kurung] seperti ini:
    ```
    (snakes) $
    ```
4. Verifikasi versi Python mana yang ada di environments kita saat ini:
    ```
    python --version
    ```
5. Nonaktifkan snakes environment dan kembali ke environments dasar: `conda activate`
</br>

## Managing packages
Di bagian ini, kita memeriksa paket mana yang telah terinstal, memeriksa mana yang tersedia dan mencari paket tertentu dan menginstalnya.

1. Untuk menemukan paket yang telah terinstal, aktifkan terlebih dahulu environments yang ingin kita cari. Lihat di atas untuk perintah untuk mengaktifkan snakes environment.

2. Periksa untuk melihat apakah paket yang belum terinstal bernama "beautifulsoup4" tersedia dari repositori Anaconda (harus terhubung ke Internet):
    ```
    conda search beautifulsoup4
    ```
    Conda menampilkan daftar semua paket dengan nama itu di repositori Anaconda.

3. Instal paket beautifulsoup4 ke environments saat ini:
    ```
    conda install beautifulsoup4
    ```
4. Periksa untuk melihat apakah program yang baru diinstal ada di environments ini:
    ```
    conda list
    ```