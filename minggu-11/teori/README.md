# Rangkuman Pertemuan 10
</br>

## Project Layout
---
Membuat environment 
```python
conda create -n workshopy
```
Mengaktifkan environment yang telah dibuat
```python
conda activate workshopy
```
Memasang paket flask
```python
conda install flask
```
Buat direktori proyek dan masukkan:
```python
$ mkdir flask-tutorial
$ cd flask-tutorial
```
Kemudian ikuti petunjuk instalasi untuk menyiapkan lingkungan virtual Python dan menginstal Flask untuk proyek Anda.

Tutorial akan menganggap Anda bekerja dari flask-tutorial direktori mulai sekarang. Nama file di bagian atas setiap blok kode relatif terhadap direktori ini.

---
Aplikasi Flask bisa sesederhana satu file.

hello.py
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```
Namun, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan paket untuk mengatur kode ke dalam beberapa modul yang dapat diimpor jika diperlukan, dan tutorial ini juga akan melakukannya.

Direktori proyek akan berisi:

- `flaskr/`, paket Python yang berisi kode aplikasi dan file Anda.

- `tests/`, direktori yang berisi modul pengujian.

- `venv/`, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.

- File instalasi memberi tahu Python cara menginstal proyek Anda.

- Konfigurasi kontrol versi, seperti git . Anda harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda, berapa pun ukurannya.

- File proyek lain yang mungkin Anda tambahkan di masa mendatang.

Pada akhirnya, tata letak proyek Anda akan terlihat seperti ini:
```python
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```
Jika Anda menggunakan kontrol versi, file berikut yang dihasilkan saat menjalankan proyek Anda harus diabaikan. Mungkin ada file lain berdasarkan editor yang Anda gunakan. Secara umum, abaikan file yang tidak Anda tulis. Misalnya, dengan git:

.gitignore
```
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```

</br>

## Application Setup
---
Aplikasi Flask adalah turunan dari Flaskkelas. Segala sesuatu tentang aplikasi, seperti konfigurasi dan URL, akan didaftarkan dengan kelas ini.

Cara paling mudah untuk membuat aplikasi Flask adalah dengan membuat Flaskinstance global langsung di bagian atas kode Anda, seperti bagaimana "Hello, World!" contoh lakukan pada halaman sebelumnya. Meskipun ini sederhana dan berguna dalam beberapa kasus, ini dapat menyebabkan beberapa masalah rumit saat proyek berkembang.

Alih-alih membuat Flaskinstance secara global, Anda akan membuatnya di dalam suatu fungsi. Fungsi ini dikenal sebagai pabrik aplikasi . Setiap konfigurasi, registrasi, dan pengaturan lain yang dibutuhkan aplikasi akan terjadi di dalam fungsi, kemudian aplikasi akan dikembalikan.

### The Application Factory

Saatnya untuk memulai pengkodean! Buat `flaskr` direktori dan tambahkan `__init__.py` file. Melayani tugas ganda : `__init__.py` itu akan berisi pabrik aplikasi, dan memberitahu Python bahwa `flaskr` direktori harus diperlakukan sebagai sebuah paket.
```
$ mkdir flaskr
```

flaskr/__init__.py
```
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

create_appadalah fungsi pabrik aplikasi. Anda akan menambahkannya nanti di tutorial, tetapi itu sudah banyak membantu.

app = Flask(__name__, instance_relative_config=True)menciptakan Flaskinstance.

__name__adalah nama modul Python saat ini. Aplikasi perlu mengetahui di mana lokasinya untuk menyiapkan beberapa jalur, dan __name__merupakan cara yang nyaman untuk memberitahukannya.

instance_relative_config=Truememberi tahu aplikasi bahwa file konfigurasi relatif terhadap folder instance . Folder instans terletak di luar flaskrpaket dan dapat menyimpan data lokal yang tidak boleh dikomit ke kontrol versi, seperti rahasia konfigurasi dan file database.

app.config.from_mapping()menyetel beberapa konfigurasi default yang akan digunakan aplikasi:

SECRET_KEYdigunakan oleh Flask dan ekstensi untuk menjaga keamanan data. Ini diatur untuk 'dev'memberikan nilai yang nyaman selama pengembangan, tetapi harus diganti dengan nilai acak saat digunakan.

DATABASEadalah jalur tempat file database SQLite akan disimpan. Itu di bawah app.instance_path, yang merupakan jalur yang telah dipilih Flask untuk folder instance. Anda akan mempelajari lebih lanjut tentang database di bagian berikutnya.

app.config.from_pyfile()menimpa konfigurasi default dengan nilai yang diambil dari config.py file di folder instance jika ada. Misalnya, saat menerapkan, ini dapat digunakan untuk mengatur file SECRET_KEY.

test_configjuga dapat diteruskan ke pabrik, dan akan digunakan sebagai pengganti konfigurasi instans. Ini agar pengujian yang akan Anda tulis nanti dalam tutorial dapat dikonfigurasi secara independen dari nilai pengembangan apa pun yang telah Anda konfigurasikan.

os.makedirs()memastikan bahwa app.instance_pathada. Flask tidak membuat folder instance secara otomatis, tetapi perlu dibuat karena proyek Anda akan membuat file database SQLite di sana.

@app.route()membuat rute sederhana sehingga Anda dapat melihat aplikasi bekerja sebelum masuk ke tutorial selanjutnya. Ini membuat koneksi antara URL /hellodan fungsi yang mengembalikan respons, string dalam kasus ini.'Hello, World!'

### Run The Application
Sekarang Anda dapat menjalankan aplikasi Anda menggunakan flaskperintah. Dari terminal, beri tahu Flask di mana menemukan aplikasi Anda, lalu jalankan dalam mode pengembangan. flask-tutorialIngat, Anda harus tetap berada di direktori tingkat atas , bukan flaskrpaket.

Mode pengembangan menampilkan debugger interaktif setiap kali halaman memunculkan pengecualian, dan memulai ulang server setiap kali Anda membuat perubahan pada kode. Anda dapat membiarkannya berjalan dan hanya memuat ulang halaman browser saat Anda mengikuti tutorial.

```bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```
Anda akan melihat output yang mirip dengan ini:
```
* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```

Kunjungi http://127.0.0.1:5000/hello di browser dan Anda akan melihat "Halo, Dunia!" pesan. Selamat, Anda sekarang menjalankan aplikasi web Flask Anda!

Jika program lain sudah menggunakan port 5000, Anda akan melihat atau saat server mencoba memulai. Lihat Alamat sudah digunakan untuk cara menanganinya.OSError: [Errno 98]OSError: [WinError 10013]

</br>

## Define and Access the Database
---
Aplikasi akan menggunakan database SQLite untuk menyimpan pengguna dan posting. Python hadir dengan dukungan bawaan untuk SQLite dalam sqlite3 modul.

SQLite nyaman karena tidak memerlukan pengaturan server database terpisah dan sudah terintegrasi dengan Python. Namun, jika permintaan bersamaan mencoba menulis ke database pada saat yang sama, permintaan tersebut akan melambat karena setiap penulisan terjadi secara berurutan. Aplikasi kecil tidak akan memperhatikan ini. Setelah Anda menjadi besar, Anda mungkin ingin beralih ke database yang berbeda.

Tutorial tidak membahas secara detail tentang SQL. Jika Anda tidak terbiasa dengannya, dokumen SQLite menjelaskan bahasanya .
### Connect to the Database
Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite (dan sebagian besar perpustakaan database Python lainnya) adalah membuat koneksi ke database tersebut. Setiap kueri dan operasi dilakukan menggunakan koneksi, yang ditutup setelah pekerjaan selesai.

Dalam aplikasi web, koneksi ini biasanya terkait dengan permintaan. Itu dibuat di beberapa titik saat menangani permintaan, dan ditutup sebelum respons dikirim.

flaskr/db.py
```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
g adalah objek khusus yang unik untuk setiap permintaan. Ini digunakan untuk menyimpan data yang mungkin diakses oleh beberapa fungsi selama permintaan. Koneksi disimpan dan digunakan kembali alih-alih membuat koneksi baru jika get_dbdipanggil untuk kedua kalinya dalam permintaan yang sama.

current_appadalah objek khusus lain yang menunjuk ke aplikasi Flask yang menangani permintaan. Karena Anda menggunakan pabrik aplikasi, tidak ada objek aplikasi saat menulis sisa kode Anda. get_dbakan dipanggil ketika aplikasi telah dibuat dan sedang menangani permintaan, sehingga current_appdapat digunakan.

sqlite3.connect()membuat koneksi ke file yang ditunjuk oleh DATABASEkunci konfigurasi. File ini belum harus ada, dan tidak akan ada sampai Anda menginisialisasi database nanti.

sqlite3.Rowmemberitahu koneksi untuk mengembalikan baris yang berperilaku seperti dicts. Hal ini memungkinkan mengakses kolom dengan nama.

close_dbmemeriksa apakah koneksi dibuat dengan memeriksa apakah g.db sudah disetel. Jika koneksi ada, itu ditutup. Lebih jauh ke bawah Anda akan memberi tahu aplikasi Anda tentang close_dbfungsi di pabrik aplikasi sehingga dipanggil setelah setiap permintaan.
### Create the Tables
Dalam SQLite, data disimpan dalam tabel dan kolom . Ini perlu dibuat sebelum Anda dapat menyimpan dan mengambil data. Flaskr akan menyimpan pengguna di usertabel, dan posting di posttabel. Buat file dengan perintah SQL yang diperlukan untuk membuat tabel kosong:

flaskr/schema.sql
```
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```
Tambahkan fungsi Python yang akan menjalankan perintah SQL ini ke db.pyfile:

flaskr/db.py
```
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
open_resource()membuka file relatif terhadap flaskrpaket, yang berguna karena Anda tidak perlu tahu di mana lokasi itu saat menerapkan aplikasi nanti. get_db mengembalikan koneksi database, yang digunakan untuk menjalankan perintah yang dibaca dari file.

click.command()mendefinisikan perintah baris perintah init-db yang memanggil init_dbfungsi dan menunjukkan pesan sukses kepada pengguna. Anda dapat membaca Antarmuka Baris Perintah untuk mempelajari lebih lanjut tentang menulis perintah.
### Register with the Application
Fungsi close_dband init_db_commandharus didaftarkan pada instance aplikasi; jika tidak, mereka tidak akan digunakan oleh aplikasi. Namun, karena Anda menggunakan fungsi pabrik, instans tersebut tidak tersedia saat menulis fungsi. Sebagai gantinya, tulis fungsi yang mengambil aplikasi dan melakukan pendaftaran.

flaskr/db.py
```
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```
app.teardown_appcontext()memberitahu Flask untuk memanggil fungsi itu saat membersihkan setelah mengembalikan respons.

app.cli.add_command()menambahkan perintah baru yang dapat dipanggil dengan flaskperintah.

Impor dan panggil fungsi ini dari pabrik. Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr/__init__.py
```
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```
### Initialize the Database File
Sekarang setelah init-dbterdaftar dengan aplikasi, itu dapat dipanggil menggunakan flaskperintah, mirip dengan runperintah dari halaman sebelumnya.

`Catatan
Jika Anda masih menjalankan server dari halaman sebelumnya, Anda dapat menghentikan server, atau menjalankan perintah ini di terminal baru. Jika Anda menggunakan terminal baru, ingatlah untuk mengubah ke direktori proyek Anda dan mengaktifkan env seperti yang dijelaskan dalam Instalasi . Anda juga harus mengatur FLASK_APPdan FLASK_ENVseperti yang ditunjukkan pada halaman sebelumnya.`

Jalankan init-dbperintah:
```
$ flask init-db
Initialized the database.
```
Sekarang akan ada flaskr.sqlitefile di instancefolder di proyek Anda.

</br>

## Blueprints and Views
---
Fungsi tampilan adalah kode yang Anda tulis untuk menanggapi permintaan ke aplikasi Anda. Flask menggunakan pola untuk mencocokkan URL permintaan yang masuk dengan tampilan yang seharusnya menanganinya. Tampilan mengembalikan data yang diubah Flask menjadi respons keluar. Flask juga bisa pergi ke arah lain dan menghasilkan URL ke tampilan berdasarkan nama dan argumennya.

### Create a Blueprint
Blueprint adalah cara untuk mengatur sekelompok tampilan terkait dan kode lainnya. Daripada mendaftarkan tampilan dan kode lain secara langsung dengan aplikasi, mereka terdaftar dengan cetak biru. Kemudian cetak biru didaftarkan dengan aplikasi ketika tersedia di fungsi pabrik.

Flaskr akan memiliki dua cetak biru, satu untuk fungsi otentikasi dan satu lagi untuk fungsi posting blog. Kode untuk setiap cetak biru akan dimasukkan ke dalam modul terpisah. Karena blog perlu mengetahui tentang autentikasi, Anda akan menulis autentikasi terlebih dahulu.

flaskr/auth.py
```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```
Ini menciptakan Blueprintbernama 'auth'. Seperti objek aplikasi, cetak biru perlu tahu di mana itu didefinisikan, sehingga __name__ diteruskan sebagai argumen kedua. Itu url_prefixakan ditambahkan ke semua URL yang terkait dengan cetak biru.

Impor dan daftarkan cetak biru dari pabrik menggunakan app.register_blueprint(). Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
Cetak biru otentikasi akan memiliki tampilan untuk mendaftarkan pengguna baru dan untuk masuk dan keluar.
### The First View: Register
Saat pengguna mengunjungi /auth/registerURL, registertampilan akan mengembalikan HTML dengan formulir untuk mereka isi. Ketika mereka mengirimkan formulir, itu akan memvalidasi input mereka dan menampilkan formulir lagi dengan pesan kesalahan atau membuat pengguna baru dan pergi ke halaman login.

Untuk saat ini Anda hanya akan menulis kode tampilan. Pada halaman berikutnya, Anda akan menulis template untuk menghasilkan formulir HTML.

flaskr/auth.py
```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
Inilah yang dilakukan registerfungsi tampilan:

1. @bp.routemengaitkan URL /register dengan registerfungsi tampilan. Ketika Flask menerima permintaan ke /auth/register, itu akan memanggil registertampilan dan menggunakan nilai kembalian sebagai respons.
2. Jika pengguna mengirimkan formulir, request.methodakan 'POST'. Dalam hal ini, mulailah memvalidasi input.
3. request.formadalah tipe khusus dari dictpemetaan kunci dan nilai formulir yang dikirimkan. Pengguna akan memasukkan usernamedan password.
4. Validasi itu usernamedan passwordjangan kosong.
5. Jika validasi berhasil, masukkan data pengguna baru ke dalam database.

   - db.executemengambil kueri SQL dengan ?placeholder untuk input pengguna apa pun, dan sejumlah nilai untuk menggantikan placeholder. Pustaka database akan menangani pelepasan nilai sehingga Anda tidak rentan terhadap serangan injeksi SQL .
   - Untuk keamanan, kata sandi tidak boleh disimpan dalam database secara langsung. Sebagai gantinya, generate_password_hash()digunakan untuk hash kata sandi dengan aman, dan hash itu disimpan. Karena kueri ini mengubah data, db.commit()perlu dipanggil setelahnya untuk menyimpan perubahan.
   - Sebuah sqlite3.IntegrityErrorakan terjadi jika nama pengguna sudah ada, yang harus ditampilkan kepada pengguna sebagai kesalahan validasi lain.

6. Setelah menyimpan pengguna, mereka diarahkan ke halaman login. url_for()menghasilkan URL untuk tampilan login berdasarkan namanya. Ini lebih baik daripada menulis URL secara langsung karena memungkinkan Anda mengubah URL nanti tanpa mengubah semua kode yang tertaut ke sana. redirect()menghasilkan respons pengalihan ke URL yang dihasilkan.
7. Jika validasi gagal, kesalahan akan ditampilkan kepada pengguna. flash() menyimpan pesan yang dapat diambil saat merender template.
8. Ketika pengguna awalnya menavigasi ke auth/register, atau ada kesalahan validasi, halaman HTML dengan formulir pendaftaran akan ditampilkan. render_template()akan merender template yang berisi HTML, yang akan Anda tulis di langkah tutorial berikutnya.
### Login
Tampilan ini mengikuti pola yang sama seperti registertampilan di atas.

flaskr/auth.py
```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```
Ada beberapa perbedaan dari registertampilan:

1. Pengguna ditanyai terlebih dahulu dan disimpan dalam variabel untuk digunakan nanti.
   
    fetchone()mengembalikan satu baris dari kueri. Jika kueri tidak memberikan hasil, kueri akan mengembalikan None. Nanti, fetchall()akan digunakan, yang mengembalikan daftar semua hasil.
    
2. check_password_hash()hash kata sandi yang dikirimkan dengan cara yang sama seperti hash yang disimpan dan membandingkannya dengan aman. Jika cocok, kata sandi valid.
3. sessionadalah dictyang menyimpan data di seluruh permintaan. Ketika validasi berhasil, pengguna iddisimpan dalam sesi baru. Data disimpan dalam cookie yang dikirim ke browser, dan browser kemudian mengirimkannya kembali dengan permintaan berikutnya. Flask menandatangani data dengan aman sehingga tidak dapat dirusak.

Sekarang setelah pengguna iddisimpan di session, itu akan tersedia pada permintaan berikutnya. Di awal setiap permintaan, jika pengguna masuk, informasi mereka harus dimuat dan tersedia untuk tampilan lain.

flaskr/auth.py
```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```

bp.before_app_request()mendaftarkan fungsi yang berjalan sebelum fungsi tampilan, apa pun URL yang diminta. load_logged_in_usermemeriksa apakah id pengguna disimpan di sessiondan mendapatkan data pengguna itu dari database, menyimpannya di g.user, yang berlangsung selama permintaan. Jika tidak ada id pengguna, atau jika id tidak ada, g.userakan menjadi None.
### Logout
Untuk keluar, Anda harus menghapus id pengguna dari file session. Kemudian load_logged_in_usertidak akan memuat pengguna pada permintaan berikutnya.

flaskr/auth.py
```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
### Require Authentication in Other Views
Membuat, mengedit, dan menghapus posting blog akan membutuhkan pengguna untuk login. Dekorator dapat digunakan untuk memeriksa ini untuk setiap tampilan yang diterapkan.

flaskr/auth.py
```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
Dekorator ini mengembalikan fungsi tampilan baru yang membungkus tampilan asli yang diterapkannya. Fungsi baru memeriksa apakah pengguna dimuat dan dialihkan ke halaman login sebaliknya. Jika pengguna dimuat, tampilan asli dipanggil dan berlanjut secara normal. Anda akan menggunakan dekorator ini saat menulis tampilan blog.
### Endpoints and URLs
Fungsi url_for()menghasilkan URL ke tampilan berdasarkan nama dan argumen. Nama yang terkait dengan tampilan juga disebut titik akhir , dan secara default sama dengan nama fungsi tampilan.

Misalnya, hello()tampilan yang ditambahkan ke pabrik aplikasi sebelumnya dalam tutorial memiliki nama 'hello'dan dapat ditautkan dengan url_for('hello'). Jika dibutuhkan argumen, yang akan Anda lihat nanti, itu akan ditautkan dengan menggunakan .url_for('hello', who='World')

Saat menggunakan cetak biru, nama cetak biru didahulukan dengan nama fungsi, jadi titik akhir untuk loginfungsi yang Anda tulis di atas adalah 'auth.login'karena Anda menambahkannya ke 'auth' cetak biru.

</br>

## Templates
---
Anda telah menulis tampilan autentikasi untuk aplikasi Anda, tetapi jika Anda menjalankan server dan mencoba membuka salah satu URL, Anda akan melihat TemplateNotFoundkesalahan. Itu karena tampilan memanggil render_template(), tetapi Anda belum menulis template. File template akan disimpan di templatesdirektori di dalam flaskrpaket.

Template adalah file yang berisi data statis serta placeholder untuk data dinamis. Sebuah template diberikan dengan data tertentu untuk menghasilkan dokumen akhir. Flask menggunakan perpustakaan template Jinja untuk merender template.

Dalam aplikasi Anda, Anda akan menggunakan template untuk merender HTML yang akan ditampilkan di browser pengguna. Di Flask, Jinja dikonfigurasi untuk autoescape data apa pun yang dirender dalam template HTML. Ini berarti aman untuk merender input pengguna; karakter apa pun yang mereka masukkan yang dapat mengacaukan HTML, seperti <dan >akan diloloskan dengan nilai aman yang terlihat sama di browser tetapi tidak menimbulkan efek yang tidak diinginkan.

Jinja terlihat dan berperilaku seperti Python. Pembatas khusus digunakan untuk membedakan sintaks Jinja dari data statis dalam template. Apa pun antara {{dan }}adalah ekspresi yang akan menjadi output ke dokumen akhir. {%dan %}menunjukkan pernyataan aliran kontrol seperti ifdan for. Tidak seperti Python, blok dilambangkan dengan tag awal dan akhir daripada lekukan karena teks statis dalam blok dapat mengubah lekukan.
### The Base Layout
Setiap halaman dalam aplikasi akan memiliki tata letak dasar yang sama di sekitar badan yang berbeda. Alih-alih menulis seluruh struktur HTML di setiap template, setiap template akan memperluas template dasar dan menimpa bagian tertentu.

flaskr/templates/base.html
```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```
gtersedia secara otomatis dalam template. Berdasarkan jika g.userdiatur (dari load_logged_in_user), nama pengguna dan tautan keluar ditampilkan, atau tautan untuk mendaftar dan masuk ditampilkan. url_for()juga tersedia secara otomatis, dan digunakan untuk menghasilkan URL ke tampilan alih-alih menuliskannya secara manual.

Setelah judul halaman, dan sebelum konten, template mengulang setiap pesan yang dikembalikan oleh get_flashed_messages(). Anda menggunakan flash()tampilan untuk menampilkan pesan kesalahan, dan ini adalah kode yang akan menampilkannya.

Ada tiga blok yang ditentukan di sini yang akan diganti di templat lain:

1. {% block title %}akan mengubah judul yang ditampilkan di tab browser dan judul jendela.
2. {% block header %}mirip dengan titletetapi akan mengubah judul yang ditampilkan pada halaman.
3. {% block content %}adalah tempat isi setiap halaman pergi, seperti formulir login atau posting blog.

Template dasar langsung di templatesdirektori. Agar yang lain tetap teratur, templat untuk cetak biru akan ditempatkan di direktori dengan nama yang sama dengan cetak biru.
### Register
flaskr/templates/auth/register.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```
{% extends 'base.html' %}memberitahu Jinja bahwa template ini harus menggantikan blok dari template dasar. Semua konten yang dirender harus muncul di dalam tag yang menggantikan blok dari template dasar.{% block %}

Pola yang berguna yang digunakan di sini adalah menempatkan di dalam . Ini akan mengatur blok judul dan kemudian menampilkan nilainya ke dalam blok header, sehingga jendela dan halaman berbagi judul yang sama tanpa menulisnya dua kali.{% block title %}{% block header %}

Tag inputmenggunakan requiredatribut di sini. Ini memberitahu browser untuk tidak mengirimkan formulir sampai kolom tersebut diisi. Jika pengguna menggunakan browser lama yang tidak mendukung atribut tersebut, atau jika mereka menggunakan sesuatu selain browser untuk membuat permintaan, Anda masih ingin memvalidasi data dalam tampilan Flask. Sangat penting untuk selalu memvalidasi data di server, bahkan jika klien juga melakukan validasi.
### Log In
Ini identik dengan templat daftar kecuali untuk judul dan tombol kirim.

flaskr/templates/auth/login.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```
### Register A User
Sekarang setelah template otentikasi ditulis, Anda dapat mendaftarkan pengguna. Pastikan server masih berjalan ( jika tidak), lalu buka http://127.0.0.1:5000/auth/register .flask run

Coba klik tombol "Daftar" tanpa mengisi formulir dan lihat bahwa browser menampilkan pesan kesalahan. Coba hapus required atribut dari register.htmltemplate dan klik "Daftar" lagi. Alih-alih browser menunjukkan kesalahan, halaman akan dimuat ulang dan kesalahan dari flash()dalam tampilan akan ditampilkan.

Isi username dan password dan Anda akan diarahkan ke halaman login. Coba masukkan nama pengguna yang salah, atau nama pengguna yang benar dan kata sandi yang salah. Jika Anda masuk, Anda akan mendapatkan kesalahan karena belum ada indextampilan untuk dialihkan.

</br>

## Static Files
---
Tampilan dan template autentikasi berfungsi, tetapi saat ini terlihat sangat sederhana. Beberapa CSS dapat ditambahkan untuk menambahkan gaya ke tata letak HTML yang Anda buat. Gaya tidak akan berubah, jadi ini adalah file statis , bukan template.

Flask secara otomatis menambahkan `static` tampilan yang mengambil jalur relatif ke `flaskr/static` direktori dan menyajikannya. Template `base.html` sudah memiliki tautan ke `style.css` file:

```html
{{ url_for('static', filename='style.css') }}
```
Selain CSS, jenis file statis lainnya mungkin file dengan fungsi JavaScript, atau gambar logo. Mereka semua ditempatkan di bawah `flaskr/static` direktori dan direferensikan dengan .`url_for('static', filename='...')`

Tutorial ini tidak berfokus pada cara menulis CSS, jadi Anda cukup menyalin yang berikut ke dalam `flaskr/static/style.cssfile`:

flaskr/static/style.css
```css
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }
```
Anda dapat menemukan versi yang kurang ringkas `style.css` dalam kode contoh .

Buka http://127.0.0.1:5000/auth/login 

Anda dapat membaca lebih lanjut tentang CSS dari dokumentasi Mozilla . Jika Anda mengubah file statis, segarkan halaman browser. Jika perubahan tidak muncul, coba bersihkan cache browser Anda.

</br>

## Blog Blueprint
---
Anda akan menggunakan teknik yang sama yang Anda pelajari saat menulis cetak biru otentikasi untuk menulis cetak biru blog. Blog harus mencantumkan semua posting, mengizinkan pengguna yang masuk untuk membuat posting, dan mengizinkan penulis posting untuk mengedit atau menghapusnya.

Saat Anda menerapkan setiap tampilan, jaga agar server pengembangan tetap berjalan. Saat Anda menyimpan perubahan Anda, coba buka URL di browser Anda dan ujilah.
### The Blueprint
Tentukan cetak biru dan daftarkan di pabrik aplikasi.
```python
flaskr/blog.py
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```
Impor dan daftarkan cetak biru dari pabrik menggunakan app.register_blueprint(). Tempatkan kode baru di akhir fungsi pabrik sebelum mengembalikan aplikasi.

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
Berbeda dengan cetak biru auth, cetak biru blog tidak memiliki file url_prefix. Jadi indextampilan akan di /, create tampilan di /create, dan seterusnya. Blog adalah fitur utama Flaskr, jadi masuk akal jika indeks blog akan menjadi indeks utama.

Namun, titik akhir untuk indextampilan yang ditentukan di bawah ini adalah blog.index. Beberapa tampilan autentikasi mengacu pada indextitik akhir biasa. app.add_url_rule() mengaitkan nama titik akhir 'index'dengan /url sehingga url_for('index')atau url_for('blog.index')keduanya akan berfungsi, menghasilkan /URL yang sama dengan cara apa pun.

Di aplikasi lain, Anda dapat memberikan cetak biru blog a url_prefixdan menentukan tampilan terpisah indexdi pabrik aplikasi, mirip dengan hellotampilan. Maka titik akhir indexdan blog.indexdan URL akan berbeda.
### Index
Indeks akan menampilkan semua posting, yang terbaru terlebih dahulu. A JOINdigunakan agar informasi penulis dari usertabel tersedia di hasil.

flaskr/blog.py
```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
flaskr/templates/blog/index.html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```
Saat pengguna masuk, headerblok menambahkan tautan ke createtampilan. Saat pengguna adalah penulis postingan, mereka akan melihat tautan “Edit” ke updatetampilan postingan tersebut. loop.lastadalah variabel khusus yang tersedia di dalam Jinja untuk loop . Ini digunakan untuk menampilkan baris setelah setiap posting kecuali yang terakhir, untuk memisahkannya secara visual.
### Create
Tampilan createberfungsi sama dengan registertampilan auth. Baik formulir ditampilkan, atau data yang diposting divalidasi dan postingan ditambahkan ke database atau kesalahan ditampilkan.

Dekorator yang login_requiredAnda tulis sebelumnya digunakan pada tampilan blog. Seorang pengguna harus login untuk mengunjungi tampilan ini, jika tidak mereka akan diarahkan ke halaman login.

flaskr/blog.py
```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```
flaskr/templates/blog/create.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```
### Update
Baik tampilan updatemaupun deletetampilan perlu diambil post oleh iddan memeriksa apakah pembuatnya cocok dengan pengguna yang masuk. Untuk menghindari duplikasi kode, Anda dapat menulis fungsi untuk mendapatkan postdan memanggilnya dari setiap tampilan.

flaskr/blog.py
```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```
abort()akan memunculkan pengecualian khusus yang mengembalikan kode status HTTP. Dibutuhkan pesan opsional untuk ditampilkan dengan kesalahan, jika tidak, pesan default akan digunakan. 404berarti “Tidak Ditemukan”, dan 403berarti “Terlarang”. ( 401berarti "Tidak Sah", tetapi Anda mengarahkan ulang ke halaman login alih-alih mengembalikan status itu.)

Argumen check_authordidefinisikan sehingga fungsi dapat digunakan untuk mendapatkan a posttanpa memeriksa pembuatnya. Ini akan berguna jika Anda menulis tampilan untuk menampilkan kiriman individual pada halaman, di mana pengguna tidak masalah karena mereka tidak mengubah kiriman.

flaskr/blog.py
```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
Berbeda dengan tampilan yang telah Anda tulis sejauh ini, updatefungsi mengambil argumen, id. Itu sesuai dengan <int:id>di rute. URL asli akan terlihat seperti /1/update. Flask akan menangkap 1, memastikan itu adalah int, dan meneruskannya sebagai idargumen. Jika Anda tidak menentukan int:dan sebaliknya melakukan <id>, itu akan menjadi string. Untuk menghasilkan URL ke halaman pembaruan, url_for()perlu diteruskan idagar tahu apa yang harus diisi: . Ini juga ada di file di atas.url_for('blog.update', id=post['id'])index.html

Tampilan createdan updatetampilannya terlihat sangat mirip. Perbedaan utama adalah bahwa updatetampilan menggunakan postobjek dan UPDATEkueri alih-alih file INSERT. Dengan beberapa pemfaktoran ulang yang cerdas, Anda dapat menggunakan satu tampilan dan template untuk kedua tindakan, tetapi untuk tutorial lebih jelas memisahkannya.

flaskr/templates/blog/update.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```
Template ini memiliki dua bentuk. Yang pertama memposting data yang diedit ke halaman saat ini ( /<id>/update). Formulir lainnya hanya berisi tombol dan menentukan actionatribut yang memposting ke tampilan hapus. Tombol menggunakan beberapa JavaScript untuk menampilkan dialog konfirmasi sebelum mengirimkan.

Pola digunakan untuk memilih data apa yang muncul dalam form. Ketika formulir belum dikirimkan, data asli muncul, tetapi jika data formulir yang tidak valid telah diposting, Anda ingin menampilkannya sehingga pengguna dapat memperbaiki kesalahan, jadi digunakan sebagai gantinya. adalah variabel lain yang secara otomatis tersedia di template.{{ request.form['title'] or post['title'] }}postrequest.formrequest
### Delete
Tampilan hapus tidak memiliki template sendiri, tombol hapus adalah bagian dari update.htmldan memposting ke /<id>/deleteURL. Karena tidak ada template, itu hanya akan menangani POSTmetode dan kemudian mengarahkan ulang ke indextampilan.

flaskr/blog.py
```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```
Selamat, Anda sekarang telah selesai menulis aplikasi Anda! Luangkan waktu untuk mencoba semua yang ada di browser. Namun, masih banyak yang harus dilakukan sebelum proyek selesai.

</br>

## Make the Project Installable
---
Membuat proyek Anda dapat diinstal berarti Anda dapat membuat file distribusi dan menginstalnya di lingkungan lain, sama seperti Anda menginstal Flask di lingkungan proyek Anda. Ini membuat penerapan proyek Anda sama dengan menginstal pustaka lain, jadi Anda menggunakan semua alat Python standar untuk mengelola semuanya.

Menginstal juga dilengkapi dengan manfaat lain yang mungkin tidak terlihat dari tutorial atau sebagai pengguna Python baru, termasuk:

- Saat ini, Python dan Flask memahami cara menggunakan flaskr paket hanya karena Anda menjalankan dari direktori proyek Anda. Menginstal berarti Anda dapat mengimpornya dari mana pun Anda menjalankannya.
- Anda dapat mengelola dependensi proyek Anda seperti halnya paket lain, jadi instal.pip install yourproject.whl
- Alat pengujian dapat mengisolasi lingkungan pengujian Anda dari lingkungan pengembangan Anda.
### Describe the Project
File setup.pymenjelaskan proyek Anda dan file miliknya.

setup.py
```py
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```
packagesmemberi tahu Python direktori paket apa (dan file Python yang dikandungnya) untuk disertakan. find_packages()menemukan direktori ini secara otomatis sehingga Anda tidak perlu mengetiknya. Untuk menyertakan file lain, seperti direktori statis dan template, include_package_datasudah diatur. Python membutuhkan file lain bernama MANIFEST.inuntuk memberi tahu apa data lain ini.

MANIFEST.in
```
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```
Ini memberitahu Python untuk menyalin semua yang ada di direktori and, dan staticfile , tetapi untuk mengecualikan semua file bytecode.templatesschema.sql

### Install the Project
Gunakan pipuntuk menginstal proyek Anda di lingkungan virtual.
```
$ pip install -e .
```
Ini memberitahu pip untuk menemukan setup.pydi direktori saat ini dan menginstalnya dalam mode yang dapat diedit atau pengembangan . Mode yang dapat diedit berarti bahwa saat Anda membuat perubahan pada kode lokal, Anda hanya perlu menginstal ulang jika Anda mengubah metadata tentang proyek, seperti dependensinya.

Anda dapat mengamati bahwa proyek tersebut sekarang diinstal dengan .pip list
```
$ pip list

Package        Version   Location
-------------- --------- ----------------------------------
click          6.7
Flask          1.0
flaskr         1.0.0     /home/user/Projects/flask-tutorial
itsdangerous   0.24
Jinja2         2.10
MarkupSafe     1.0
pip            9.0.3
setuptools     39.0.1
Werkzeug       0.14.1
wheel          0.30.0
```
Tidak ada yang berubah dari cara Anda menjalankan proyek sejauh ini. FLASK_APPmasih disetel ke flaskrdan masih menjalankan aplikasi, tetapi Anda dapat memanggilnya dari mana saja, bukan hanya direktori.flask runflask-tutorial

</br>

## Test Coverage
---
Menulis pengujian unit untuk aplikasi Anda memungkinkan Anda memeriksa apakah kode yang Anda tulis berfungsi seperti yang Anda harapkan. Flask menyediakan klien uji yang mensimulasikan permintaan ke aplikasi dan mengembalikan data respons.

Anda harus menguji sebanyak mungkin kode Anda. Kode dalam fungsi hanya berjalan ketika fungsi dipanggil, dan kode di cabang, seperti if blok, hanya berjalan ketika kondisi terpenuhi. Anda ingin memastikan bahwa setiap fungsi diuji dengan data yang mencakup setiap cabang.

Semakin dekat Anda mencapai cakupan 100%, semakin nyaman Anda karena membuat perubahan tidak akan mengubah perilaku orang lain secara tiba-tiba. Namun, cakupan 100% tidak menjamin bahwa aplikasi Anda tidak memiliki bug. Secara khusus, itu tidak menguji bagaimana pengguna berinteraksi dengan aplikasi di browser. Meskipun demikian, cakupan pengujian merupakan alat penting untuk digunakan selama pengembangan.

Anda akan menggunakan pytest dan coverage untuk menguji dan mengukur kode Anda. Instal keduanya:
```
$ pip install pytest coverage
```
### Setup and Fixtures
Kode tes terletak di testsdirektori. Direktori ini berada di sebelah paket flaskr, bukan di dalamnya. File tests/conftest.pyberisi fungsi pengaturan yang disebut perlengkapan yang akan digunakan setiap pengujian. Pengujian dalam modul Python yang dimulai dengan test_, dan setiap fungsi pengujian dalam modul tersebut juga dimulai dengan test_.

Setiap pengujian akan membuat file database sementara baru dan mengisi beberapa data yang akan digunakan dalam pengujian. Tulis file SQL untuk memasukkan data itu.

tests/data.sql
```sql
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```
Fixture appakan memanggil pabrik dan lolos test_configuntuk mengonfigurasi aplikasi dan database untuk pengujian alih-alih menggunakan konfigurasi pengembangan lokal Anda.

tests/conftest.py
```py
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```
tempfile.mkstemp()membuat dan membuka file sementara, mengembalikan deskriptor file dan jalur ke sana. Jalur DATABASEdiganti sehingga mengarah ke jalur sementara ini alih-alih folder instance. Setelah mengatur jalur, tabel database dibuat dan data uji dimasukkan. Setelah tes selesai, file sementara ditutup dan dihapus.

TESTINGmemberitahu Flask bahwa aplikasi dalam mode uji. Flask mengubah beberapa perilaku internal sehingga lebih mudah untuk diuji, dan ekstensi lain juga dapat menggunakan tanda untuk mempermudah pengujian.

Fixture clientmemanggil app.test_client()dengan objek aplikasi yang dibuat oleh appfixture. Pengujian akan menggunakan klien untuk membuat permintaan ke aplikasi tanpa menjalankan server.

Perlengkapannya runnermirip dengan client. app.test_cli_runner()membuat pelari yang dapat memanggil perintah Klik yang terdaftar dengan aplikasi.

Pytest menggunakan perlengkapan dengan mencocokkan nama fungsinya dengan nama argumen dalam fungsi pengujian. Misalnya, test_hello fungsi yang akan Anda tulis selanjutnya membutuhkan clientargumen. Pytest mencocokkannya dengan clientfungsi fixture, memanggilnya, dan meneruskan nilai yang dikembalikan ke fungsi pengujian.
### Factory
Tidak banyak yang bisa diuji tentang pabrik itu sendiri. Sebagian besar kode akan dieksekusi untuk setiap tes, jadi jika ada yang gagal, tes lain akan memperhatikan.

Satu-satunya perilaku yang dapat berubah adalah melewati konfigurasi pengujian. Jika konfigurasi tidak diteruskan, harus ada beberapa konfigurasi default, jika tidak, konfigurasi harus diganti.

tests/test_factory.py
```py
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```
Anda menambahkan hellorute sebagai contoh saat menulis pabrik di awal tutorial. Ini mengembalikan "Halo, Dunia!", Jadi tes memeriksa apakah data respons cocok.
### Database
Dalam konteks aplikasi, get_dbharus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah konteksnya, koneksi harus ditutup.

tests/test_db.py
```py
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```
Perintah init-dbharus memanggil init_dbfungsi dan mengeluarkan pesan.

tests/test_db.py
```py
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```
Tes ini menggunakan monkeypatchperlengkapan Pytest untuk mengganti init_dbfungsi dengan yang mencatat bahwa itu telah dipanggil. Perlengkapan runneryang Anda tulis di atas digunakan untuk memanggil init-db perintah dengan nama.
### Authentication
Untuk sebagian besar tampilan, pengguna harus masuk. Cara termudah untuk melakukan ini dalam pengujian adalah membuat POSTpermintaan ke logintampilan dengan klien. Daripada menuliskannya setiap saat, Anda dapat menulis kelas dengan metode untuk melakukan itu, dan menggunakan perlengkapan untuk memberikannya kepada klien untuk setiap pengujian.

tests/conftest.py
```py
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
```
Dengan authperlengkapan, Anda dapat memanggil auth.login()tes untuk masuk sebagai testpengguna, yang dimasukkan sebagai bagian dari data uji di appperlengkapan.

Tampilan registerharus berhasil dirender pada GET. Aktif POST dengan data formulir yang valid, itu harus diarahkan ke URL login dan data pengguna harus ada di database. Data yang tidak valid harus menampilkan pesan kesalahan.

tests/test_auth.py
```py
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```
client.get()membuat GETpermintaan dan mengembalikan Responseobjek yang dikembalikan oleh Flask. Demikian pula, client.post()membuat POST permintaan, mengubah datadict menjadi data formulir.

Untuk menguji apakah halaman berhasil dirender, permintaan sederhana dibuat dan diperiksa untuk file . Jika rendering gagal, Flask akan mengembalikan kode.200 OK status_code500 Internal Server Error

headersakan memiliki Locationheader dengan URL login saat tampilan register dialihkan ke tampilan login.

databerisi badan respons sebagai byte. Jika Anda mengharapkan nilai tertentu untuk dirender pada laman, periksa apakah nilai tersebut dalam data. Bytes harus dibandingkan dengan byte. Jika Anda ingin membandingkan teks, gunakan get_data(as_text=True) sebagai gantinya.

pytest.mark.parametrizememberitahu Pytest untuk menjalankan fungsi pengujian yang sama dengan argumen yang berbeda. Anda menggunakannya di sini untuk menguji berbagai masukan tidak valid dan pesan kesalahan tanpa menulis kode yang sama tiga kali.

Pengujian untuk logintampilan sangat mirip dengan pengujian untuk register. Daripada menguji data dalam database, sessionharus user_idmengatur setelah login.

tests/test_auth.py
```py
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
```
Menggunakan clientdi withblok memungkinkan mengakses variabel konteks seperti sessionsetelah respons dikembalikan. Biasanya, mengakses sessiondi luar permintaan akan menimbulkan kesalahan.

Pengujian logoutadalah kebalikan dari login. sessiontidak boleh berisi user_idsetelah logout.

tests/test_auth.py
```py
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```
### Blog
Semua tampilan blog menggunakan authperlengkapan yang Anda tulis sebelumnya. Panggilan auth.login()dan permintaan berikutnya dari klien akan masuk sebagai testpengguna.

Tampilan indexharus menampilkan informasi tentang postingan yang ditambahkan dengan data pengujian. Saat masuk sebagai penulis, harus ada tautan untuk mengedit posting.

Anda juga dapat menguji beberapa perilaku autentikasi lagi saat menguji indextampilan. Saat tidak masuk, setiap halaman menampilkan tautan untuk masuk atau mendaftar. Saat masuk, ada tautan untuk keluar.

tests/test_blog.py
```py
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```
Pengguna harus masuk untuk mengakses create, update, dan deletetampilan. Pengguna yang masuk harus menjadi penulis kiriman untuk mengakses updatedan delete, jika tidak, status akan dikembalikan. Jika a dengan yang diberikan tidak ada, dan harus kembali .403 Forbiddenpostidupdatedelete404 Not Found

tests/test_blog.py
```py
@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```
Tampilan createand updateharus merender dan mengembalikan status untuk permintaan. Ketika data yang valid dikirim dalam permintaan, harus memasukkan data posting baru ke dalam database, dan harus mengubah data yang ada. Kedua halaman harus menampilkan pesan kesalahan pada data yang tidak valid.200 OKGETPOSTcreateupdate

tests/test_blog.py
```py
def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data
```
Tampilan deleteharus dialihkan ke URL indeks dan pos seharusnya tidak ada lagi di database.

tests/test_blog.py
```py
def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```
### Running the Tests
Beberapa konfigurasi tambahan, yang tidak diperlukan tetapi membuat pengujian berjalan dengan cakupan yang lebih sedikit, dapat ditambahkan ke file proyek setup.cfg.

setup.cfg
```cfg
[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source =
    flaskr
```
Untuk menjalankan tes, gunakan pytestperintah. Ini akan menemukan dan menjalankan semua fungsi pengujian yang telah Anda tulis.
```bash
$ pytest

========================= test session starts ==========================
platform linux -- Python 3.6.4, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
rootdir: /home/user/Projects/flask-tutorial, inifile: setup.cfg
collected 23 items

tests/test_auth.py ........                                      [ 34%]
tests/test_blog.py ............                                  [ 86%]
tests/test_db.py ..                                              [ 95%]
tests/test_factory.py ..                                         [100%]

====================== 24 passed in 0.64 seconds =======================
``` 
Jika ada tes yang gagal, pytest akan menunjukkan kesalahan yang muncul. Anda dapat menjalankan untuk mendapatkan daftar setiap fungsi pengujian daripada titik.pytest -v

Untuk mengukur cakupan kode pengujian Anda, gunakan coverageperintah untuk menjalankan pytest alih-alih menjalankannya secara langsung.
```
$ coverage run -m pytest
```
Anda dapat melihat laporan cakupan sederhana di terminal:
```bash
$ coverage report

Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
flaskr/__init__.py      21      0      2      0   100%
flaskr/auth.py          54      0     22      0   100%
flaskr/blog.py          54      0     16      0   100%
flaskr/db.py            24      0      4      0   100%
------------------------------------------------------
TOTAL                  153      0     44      0   100%
```
Laporan HTML memungkinkan Anda melihat baris mana yang tercakup dalam setiap file:
```
$ coverage html
```
Ini menghasilkan file dalam htmlcovdirektori. Buka htmlcov/index.htmldi browser Anda untuk melihat laporan.

</br>

## Deploy to Production
---
Bagian dari tutorial ini mengasumsikan Anda memiliki server yang ingin Anda gunakan untuk menyebarkan aplikasi Anda. Ini memberikan gambaran umum tentang cara membuat file distribusi dan menginstalnya, tetapi tidak akan membahas secara spesifik tentang server atau perangkat lunak apa yang digunakan. Anda dapat menyiapkan lingkungan baru di komputer pengembangan Anda untuk mencoba petunjuk di bawah ini, tetapi mungkin sebaiknya tidak menggunakannya untuk menghosting aplikasi publik yang sebenarnya. Lihat Opsi Penerapan untuk daftar berbagai cara untuk menghosting aplikasi Anda.
### Build and Install
Saat Anda ingin menyebarkan aplikasi Anda di tempat lain, Anda membangun file distribusi. Standar saat ini untuk distribusi Python adalah format roda , dengan .whlekstensi. Pastikan perpustakaan roda diinstal terlebih dahulu:
```
$ pip install wheel
```
Menjalankan setup.pydengan Python memberi Anda alat baris perintah untuk mengeluarkan perintah terkait build. Perintah bdist_wheelakan membangun file distribusi roda.
```
$ python setup.py bdist_wheel
```
Anda dapat menemukan file di `dist/flaskr-1.0.0-py3-none-any.whl`. Nama file dalam format {project name}-{version}-{python tag} -{abi tag}-{platform tag}.

Salin file ini ke komputer lain, siapkan virtualenv baru , lalu instal file dengan ekstensi pip.
```
$ pip install flaskr-1.0.0-py3-none-any.whl
```
Pip akan menginstal proyek Anda beserta dependensinya.

Karena ini adalah mesin yang berbeda, Anda perlu menjalankannya init-dblagi untuk membuat database di folder instance.

BASH
```BASH
$ export FLASK_APP=flaskr
$ flask init-db
```
Ketika Flask mendeteksi bahwa itu diinstal (tidak dalam mode yang dapat diedit), ia menggunakan direktori yang berbeda untuk folder instance. Anda dapat menemukannya di venv/var/flaskr-instancesebagai gantinya.
### Configure the Secret Key
Di awal tutorial yang Anda berikan nilai default untuk SECRET_KEY. Ini harus diubah menjadi beberapa byte acak dalam produksi. Jika tidak, penyerang dapat menggunakan kunci publik 'dev'untuk memodifikasi cookie sesi, atau apa pun yang menggunakan kunci rahasia.

Anda dapat menggunakan perintah berikut untuk menampilkan kunci rahasia acak:
```
$ python -c 'import secrets; print(secrets.token_hex())'

'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```
Buat config.pyfile di folder instance, yang akan dibaca oleh pabrik jika ada. Salin nilai yang dihasilkan ke dalamnya.

venv/var/flaskr-instance/config.py
```py
SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```
Anda juga dapat mengatur konfigurasi lain yang diperlukan di sini, meskipun SECRET_KEYini adalah satu-satunya yang diperlukan untuk Flaskr.

### Run with a Production Server
Saat menjalankan secara publik alih-alih dalam pengembangan, Anda tidak boleh menggunakan server pengembangan bawaan ( ). Server pengembangan disediakan oleh Werkzeug untuk kenyamanan, tetapi tidak dirancang untuk menjadi sangat efisien, stabil, atau aman.flask run

Sebagai gantinya, gunakan server WSGI produksi. Misalnya, untuk menggunakan Waitress , instal terlebih dahulu di lingkungan virtual:
```
$ pip install waitress
```
Anda perlu memberi tahu Waitress tentang aplikasi Anda, tetapi aplikasi itu tidak menggunakan FLASK_APPlike . Anda perlu memberitahunya untuk mengimpor dan memanggil pabrik aplikasi untuk mendapatkan objek aplikasi.flask run
```
$ waitress-serve --call 'flaskr:create_app'
```
Serving on http://0.0.0.0:8080
Lihat Opsi Penerapan untuk daftar berbagai cara untuk menghosting aplikasi Anda. Pelayan hanyalah sebuah contoh, dipilih untuk tutorial karena mendukung Windows dan Linux. Ada banyak lagi server WSGI dan opsi penerapan yang dapat Anda pilih untuk proyek Anda.

</br>

## Keep Developing!
---
Anda telah belajar tentang beberapa konsep Flask dan Python di sepanjang tutorial. Kembali dan tinjau tutorial dan bandingkan kode Anda dengan langkah-langkah yang Anda ambil untuk sampai ke sana. Bandingkan proyek Anda dengan proyek contoh , yang mungkin terlihat sedikit berbeda karena sifat tutorial langkah demi langkah.

Ada lebih banyak hal di Flask daripada yang Anda lihat sejauh ini. Meski begitu, Anda sekarang siap untuk mulai mengembangkan aplikasi web Anda sendiri. Lihat Quickstart untuk ikhtisar tentang apa yang dapat dilakukan Flask, lalu pelajari dokumen untuk terus belajar. Flask menggunakan Jinja , Click , Werkzeug , dan ItsDangerous di belakang layar, dan mereka semua juga memiliki dokumentasinya sendiri. Anda juga akan tertarik dengan Ekstensi yang membuat tugas seperti bekerja dengan database atau memvalidasi data formulir lebih mudah dan lebih kuat.

Jika Anda ingin terus mengembangkan proyek Flaskr Anda, berikut adalah beberapa ide untuk dicoba selanjutnya:

- Tampilan detail untuk menampilkan satu postingan. Klik judul postingan untuk membuka halamannya.
- Suka / tidak suka posting.
- Komentar.
- Tag. Mengklik tag menunjukkan semua posting dengan tag itu.
- Kotak pencarian yang memfilter halaman indeks berdasarkan nama.
- Tampilan halaman. Hanya tampilkan 5 posting per halaman.
- Unggah gambar untuk disertakan dengan postingan.
- Format posting menggunakan penurunan harga.
- Umpan RSS dari posting baru.

Bersenang-senang dan buat aplikasi yang luar biasa!