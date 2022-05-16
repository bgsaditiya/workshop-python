# Rangkuman Pertemuan 9
</br>

## Bangun Aplikasi Python dengan CockroachDB dan psycopg2
---
Tutorial ini menunjukkan bagaimana membangun aplikasi Python sederhana dengan CockroachDB dan driver psycopg2

</br>

## Langkah 1. Mulai CockroachDB
---
### Buat cluster gratis
1. Jika Anda belum melakukannya, daftar akun CockroachDB Cloud.
2. Masuk ke akun Cloud CockroachDB Anda.
3. Pada halaman Cluster , klik Buat Cluster.
4. Pada halaman Buat kluster Anda , pilih Tanpa Server.
   Kecuali Anda mengubah anggaran bulanan, cluster ini akan gratis selamanya.

5. Klik Buat kluster. 
   Cluster Anda akan dibuat dalam beberapa detik dan dialog Buat pengguna SQL akan ditampilkan.

### Buat pengguna SQL
Dialog Buat pengguna SQL memungkinkan Anda membuat pengguna dan kata sandi SQL baru.

1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.

4. Klik Berikutnya.

Saat ini, semua pengguna baru dibuat dengan hak penuh. Untuk informasi selengkapnya dan untuk mengubah setelan default, lihat Memberikan hak istimewa dan Menggunakan peran .

### Dapatkan sertifikat root
Dialog Hubungkan ke klaster menampilkan informasi tentang cara menghubungkan ke klaster Anda.
1. Pilih String koneksi umum dari dropdown Pilih opsi.
2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

### Dapatkan string koneksi
Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

</br>

## Langkah 2. Dapatkan kode sampel
---
Kloning repo GitHub kode sampel:
```python
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```
Kode sampel di example.pymelakukan hal berikut:
- Membuat accountstabel dan menyisipkan beberapa baris
- Mentransfer dana antara dua akun dalam suatu transaksi
- Hapus akun dari tabel sebelum keluar sehingga dapat menjalankan kembali kode contoh

Untuk menangani kesalahan percobaan ulang transaksi , kode menggunakan pengulangan percobaan tingkat aplikasi yang, jika terjadi kesalahan, tidur sebelum mencoba transfer dana lagi. Jika menemukan kesalahan coba lagi, ia tidur untuk interval yang lebih lama, menerapkan backoff eksponensial.

</br>

## Langkah 3. Instal driver psycopg2
---
psycopg2-binaryadalah satu-satunya dependensi modul pihak ketiga aplikasi sampel.

Untuk menginstal psycopg2-binary, jalankan perintah berikut:
```python
$ pip install psycopg2-binary
```

</br>

## Langkah 4. Jalankan kode
---
1. Setel DATABASE_URLvariabel lingkungan ke string koneksi ke cluster CockroachDB Cloud Anda:
   ```python
   $ export DATABASE_URL="{connection-string}"
   ```
   Di mana {connection-string}string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

    Aplikasi menggunakan string koneksi yang disimpan ke DATABASE_URLvariabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.
2. Jalankan kode:
   ```python
   $ cd hello-world-python-psycopg2
   ```
   ```python
   $ python example.py
   ```
   Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:
   ```
   Balances at Fri Oct 30 18:27:00 2020:
   (1, 1000)
   (2, 250)
   Balances at Fri Oct 30 18:27:00 2020:
   (1, 900)
   (2, 350)
   ```
---

   </br>

## Bangun Aplikasi Python CRUD Sederhana dengan CockroachDB dan SQLAlchemy
---

</br>

## Langkah 1. Mulai CockroachDB
---
### Buat cluster gratis
1. Jika Anda belum melakukannya, daftar akun CockroachDB Cloud.
2. Masuk ke akun Cloud CockroachDB Anda.
3. Pada halaman Cluster , klik Buat Cluster.
4. Pada halaman Buat kluster Anda , pilih Tanpa Server.
   Kecuali Anda mengubah anggaran bulanan, cluster ini akan gratis selamanya.

5. Klik Buat kluster. 
   Cluster Anda akan dibuat dalam beberapa detik dan dialog Buat pengguna SQL akan ditampilkan.

### Buat pengguna SQL
Dialog Buat pengguna SQL memungkinkan Anda membuat pengguna dan kata sandi SQL baru.

1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.

4. Klik Berikutnya.

Saat ini, semua pengguna baru dibuat dengan hak penuh. Untuk informasi selengkapnya dan untuk mengubah setelan default, lihat Memberikan hak istimewa dan Menggunakan peran.

### Dapatkan sertifikat root
Dialog Hubungkan ke klaster menampilkan informasi tentang cara menghubungkan ke klaster Anda.
1. Pilih String koneksi umum dari dropdown Pilih opsi.
2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

### Dapatkan string koneksi
Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

</br>

## Langkah 2. Dapatkan kodenya
---
Kloning repo GitHub:
```python
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```
Proyek ini memiliki struktur direktori berikut:
```
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```
File requirements.txttersebut menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk sqlalchemy-cockroachdbpaket Python , yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL:
```
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```
File dbinit.sqlmenginisialisasi skema database yang digunakan aplikasi:
```python
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```
Menggunakan SQLAlchemy models.pyuntuk memetakan Accountstabel ke objek Python:
```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```
Menggunakan SQLAlchemy main.pyuntuk memetakan metode Python ke operasi SQL:
```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```
main.pyjuga mengeksekusi mainmetode program.

</br>

## Langkah 3. Instal persyaratan aplikasi
---
Tutorial ini digunakan virtualenvuntuk manajemen ketergantungan.
1. Instal virtualenv:
   ```python
   $ pip install virtualenv
   ```
2. Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual:
   ```python
   $ virtualenv env
   ```
   ```python
   $ source env/bin/activate
   ```
3. Instal modul yang diperlukan ke lingkungan virtual:
   ```python
   $ pip install -r requirements.txt
   ```

   </br>

## Langkah 4. Inisialisasi database
---
1. Setel DATABASE_URLvariabel lingkungan ke string koneksi untuk cluster Anda:
   ```python
   $ export DATABASE_URL="{connection-string}"
   ```
   Di mana `{connection-string}` string koneksi yang Anda peroleh dari CockroachDB Cloud Console.
2. Untuk menginisialisasi database contoh, gunakan cockroach sqlperintah untuk mengeksekusi pernyataan SQL dalam `dbinit.sqlfile`:
   ```python
   $ cat dbinit.sql | cockroach sql --url $DATABASE_URL
   ```
   Pernyataan SQL dalam file inisialisasi harus dijalankan:
   ```
   CREATE TABLE
   
   Time: 102ms
   ```

</br>
   
## Langkah 5. Jalankan kodenya
---
`main.py` menggunakan string koneksi yang disimpan ke `DATABASE_URL` variabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan aplikasi:
   ```python
   $ python main.py
   ```
Aplikasi akan terhubung ke CockroachDB, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti ini:
```
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```
Dalam shell SQL yang terhubung ke cluster, Anda dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus:
```python
> SELECT COUNT(*) FROM accounts;
```
```
  count
---------
     95
(1 row)
```