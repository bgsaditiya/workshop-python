# Rangkuman Pertemuan 12
</br>

## Object creation
---
Membuat sebuah `Series` dengan meneruskan daftar nilai, membiarkan panda membuat indeks integer default:
```py
s = pd.Series([1, 3, 5, np.nan, 6, 8])

s
```
Membuat sebuah `DataFrame` dengan melewatkan array NumPy, dengan indeks datetime dan kolom berlabel:
```py
dates = pd.date_range("20130101", periods=6)

dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df
```
Membuat `DataFrame` dengan melewatkan kamus objek yang dapat diubah menjadi struktur seperti seri:
```py
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

df2
```
Kolom yang dihasilkan `DataFrame` memiliki tipe d yang berbeda :
```py
df2.dtypes
```
`dtypes digunakan untuk mengecek tipe data untuk tiap kolom di dataframe. Bisa juga digunakan untuk mengecek tipe data salah satu kolom.`

Jika Anda menggunakan IPython, penyelesaian tab untuk nama kolom (serta atribut publik) diaktifkan secara otomatis. Berikut adalah subset dari atribut yang akan diselesaikan:
```py
df2.<TAB>
```
Seperti yang terlihat, kolom A, B, C, dan D secara otomatis tab selesai. E dan F ada juga; atribut lainnya telah dipotong untuk singkatnya.

</br>

## Viewing data
---
Berikut adalah cara melihat baris atas dan bawah bingkai:
```py
df.head()

df.tail(3)
```
`head(n) akan menampilkan 5 baris data teratas, jika parameter n tidak diisi.`

`tail(n), Sama dengan head, jika fungsi tail dipanggil langsung tanpa parameter maka 5 data terakhir akan ditampilkan.`

`tail(3), Parameter diisi untuk menampilkan 3 data terakhir.`

Menampilkan indeks, kolom:
```py
df.index

df.columns
```
`DataFrame.to_numpy()` memberikan representasi NumPy dari data yang mendasarinya. Perhatikan bahwa ini bisa menjadi operasi yang mahal ketika `DataFrame` memiliki kolom dengan tipe data yang berbeda, yang menghasilkan perbedaan mendasar antara pandas dan NumPy: NumPy array memiliki satu dtype untuk seluruh array, sedangkan pandas DataFrames memiliki satu dtype per column . Saat Anda memanggil `DataFrame.to_numpy()`, pandas akan menemukan dtype NumPy yang dapat menampung semua dtypes di DataFrame. Ini mungkin berakhir menjadi object, yang membutuhkan casting setiap nilai ke objek Python.

`Fungsi index digunakan untuk mengetahui indeks pada dataframe`

`columns digunakan untuk menampilkan nama-nama kolom pada dataframe.`

Untuk df,  `DataFrame` dari semua nilai floating-point kami, `DataFrame.to_numpy()` cepat dan tidak memerlukan penyalinan data:
```py
df.to_numpy()
```
`to_numpy() adalah metode bawaan yang digunakan untuk mengonversi DataFrame menjadi array numpy.`

Untuk df2, `DataFrame` dengan beberapa tipe d, `DataFrame.to_numpy()` relatif mahal:
```py
df2.to_numpy()
```
`describe()` menunjukkan ringkasan statistik cepat dari data Anda:
```py
df.describe()
```
Mentransfer data Anda:
```py
df.T
```
Mengurutkan menurut sumbu:
```py
df.sort_index(axis=1, ascending=False)
```
Mengurutkan berdasarkan nilai:
```py
df.sort_values(by="B")
```

</br>

## Selection
---

### Getting
Memilih satu kolom, yang menghasilkan Series, setara dengan df.A:
```py
df["A"]
```
Memilih melalui [], yang mengiris baris:
```py
df[0:3]

df["20130102":"20130104"]
```

### Selection by label
Untuk mendapatkan penampang menggunakan label:
```py
df.loc[dates[0]]
```
Memilih pada multi-sumbu dengan label:
```py
df.loc[:, ["A", "B"]]
```
Menampilkan pemotongan label, kedua titik akhir disertakan :
```py
df.loc["20130102":"20130104", ["A", "B"]]
```
Pengurangan dimensi objek yang dikembalikan:
```py
df.loc["20130102", ["A", "B"]]
```
Untuk mendapatkan nilai skalar:
```py
df.loc[dates[0], "A"]
```
Untuk mendapatkan akses cepat ke skalar (setara dengan metode sebelumnya):
```py
df.at[dates[0], "A"]
```
`loc digunakan untuk mengakses data berdasarkan label (nama kolom).`

### Selection by position
Pilih melalui posisi bilangan bulat yang diteruskan:
```py
df.iloc[3]
```
Dengan irisan bilangan bulat, bertindak mirip dengan NumPy/Python:
```py
df.iloc[3:5, 0:2]
```
Dengan daftar lokasi posisi bilangan bulat, mirip dengan gaya NumPy/Python:
```py
df.iloc[[1, 2, 4], [0, 2]]
```
Untuk mengiris baris secara eksplisit:
```py
df.iloc[1:3, :]
```
Untuk mengiris kolom secara eksplisit:
```py
df.iloc[:, 1:3]
```
Untuk mendapatkan nilai secara eksplisit:
```py
df.iloc[1, 1]
```
Untuk mendapatkan akses cepat ke skalar (setara dengan metode sebelumnya):
```py
df.iat[1, 1]
```
`iloc digunakan untuk mengakses data berdasarkan posisi.`

### Boolean indexing
Menggunakan nilai kolom tunggal untuk memilih data:
```py
df[df["A"] > 0]
```
Memilih nilai dari DataFrame tempat kondisi boolean terpenuhi:
```py
df[df > 0]
```
Menggunakan metode isin() penyaringan:
```py
df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2

df2[df2["E"].isin(["two", "four"])]
```
`isin() digunakan untuk mengecek apakah ada elemen tertentu di dalam dataframe. Function ini mengembalikan nilai Boolean, True atau False, untuk tiap elemen pada dataframe.`

### Setting
Menyetel kolom baru secara otomatis menyelaraskan data dengan indeks:
```py
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

s1

df["F"] = s1
```
Menetapkan nilai menurut label:
```py
df.at[dates[0], "A"] = 0
```
Menetapkan nilai berdasarkan posisi:
```py
df.iat[0, 1] = 0
```
Pengaturan dengan menetapkan dengan array NumPy:
```py
df.loc[:, "D"] = np.array([5] * len(df))
```
Hasil dari operasi pengaturan sebelumnya:
```py
df
```
Operasi `where` dengan pengaturan:
```py
df2 = df.copy()

df2[df2 > 0] = -df2

df2
```

</br>

## Missing data
---
pandas terutama menggunakan nilai np.nan untuk mewakili data yang hilang. Ini secara default tidak termasuk dalam perhitungan.

Pengindeksan ulang memungkinkan kita untuk mengubah/menambah/menghapus indeks pada sumbu tertentu. Ini mengembalikan salinan data:
```py
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

df1.loc[dates[0] : dates[1], "E"] = 1

df1
```
Untuk menghapus setiap baris yang memiliki data yang hilang:
```py
df1.dropna(how="any")
```
Mengisi data yang hilang:
```py
df1.fillna(value=5)
```
Untuk mendapatkan topeng boolean di mana nilainya adalah nan:
```py
pd.isna(df1)
```

</br>

## Operations
---
### Stats
Operasi pada umumnya mengecualikan data yang hilang.

Melakukan statistik deskriptif:
```py
df.mean()
```
Operasi yang sama pada sumbu lainnya:
```py
df.mean(1)
```
Beroperasi dengan objek yang memiliki dimensi berbeda dan membutuhkan penyelarasan. Selain itu, panda secara otomatis menyiarkan sepanjang dimensi yang ditentukan:
```py
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

s

df.sub(s, axis="index")
```
### Apply
Menerapkan fungsi ke data:
```py
df.apply(np.cumsum)

df.apply(lambda x: x.max() - x.min())
```
### Histogramming
```py
s = pd.Series(np.random.randint(0, 7, size=10))

s

s.value_counts()
```
### String Methods
Seri dilengkapi dengan sekumpulan metode pemrosesan string dalam str atribut yang memudahkan pengoperasian pada setiap elemen larik, seperti pada cuplikan kode di bawah ini. Perhatikan bahwa pencocokan pola pada strumumnya menggunakan ekspresi reguler secara default (dan dalam beberapa kasus selalu menggunakannya).
```py
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

s.str.lower()
```

</br>

## Merge
---
### Concat
pandas menyediakan berbagai fasilitas untuk dengan mudah menggabungkan objek Seri dan DataFrame dengan berbagai jenis logika yang ditetapkan untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi tipe gabungan/gabung.

Menggabungkan objek panda bersama dengan concat():
```py
df = pd.DataFrame(np.random.randn(10, 4))

df

pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)
```
`Menambahkan kolom ke a DataFramerelatif cepat. Namun, menambahkan baris memerlukan salinan, dan mungkin mahal. Kami merekomendasikan untuk meneruskan daftar rekaman yang sudah dibuat sebelumnya ke DataFramekonstruktor alih-alih membangun a DataFramedengan menambahkan rekaman secara iteratif ke dalamnya.`
### Join
Penggabungan gaya SQL.
```py
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

left

right

pd.merge(left, right, on="key")
```
Contoh lain yang dapat diberikan adalah:
```py
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

left

right

pd.merge(left, right, on="key")
```

</br>

## Grouping
---
Dengan "mengelompokkan menurut" kami mengacu pada proses yang melibatkan satu atau lebih dari langkah-langkah berikut:
- Membagi data menjadi beberapa kelompok berdasarkan beberapa kriteria
- Menerapkan fungsi ke setiap grup secara mandiri
- Menggabungkan hasil ke dalam struktur data

```py
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)


df
```
Mengelompokkan dan kemudian menerapkan `sum()` fungsi ke grup yang dihasilkan:
```py
df.groupby("A").sum()
```
Pengelompokan berdasarkan beberapa kolom membentuk indeks hierarkis, dan sekali lagi kita dapat menerapkan sum()fungsinya:
```py
df.groupby(["A", "B"]).sum()
```
`sum() digunakan untuk menjumlahkan bilangan numerik pada dataframe berdasarkan kolom.`

</br>

## Reshaping
---
### Stack
```py
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]

df2
```
Metode stack()"memampatkan" level di kolom DataFrame:
```py
stacked = df2.stack()

stacked
```
Dengan DataFrame atau Seri "bertumpuk" (memiliki a MultiIndexsebagai index), operasi kebalikan dari stack()adalah unstack(), yang secara default membongkar level terakhir :
```py
stacked.unstack()

stacked.unstack(1)

stacked.unstack(0)
```
### Pivot tables
```py
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)


df
```
Kita dapat membuat tabel pivot dari data ini dengan sangat mudah:
```py
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
```

</br>

## Time series
---
pandas memiliki fungsionalitas yang sederhana, kuat, dan efisien untuk melakukan operasi pengambilan sampel ulang selama konversi frekuensi (misalnya, mengubah data kedua menjadi data 5 menit). Ini sangat umum, tetapi tidak terbatas pada, aplikasi keuangan.
```py
rng = pd.date_range("1/1/2012", periods=100, freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts.resample("5Min").sum()
```
Representasi zona waktu:
```py
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

ts = pd.Series(np.random.randn(len(rng)), rng)

ts

ts_utc = ts.tz_localize("UTC")

ts_utc
```
Mengonversi ke zona waktu lain:
```py
ts_utc.tz_convert("US/Eastern")
```
Mengonversi antara representasi rentang waktu:
```py
rng = pd.date_range("1/1/2012", periods=5, freq="M")

ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts

ps = ts.to_period()

ps

ps.to_timestamp()
```
Konversi antara periode dan stempel waktu memungkinkan beberapa fungsi aritmatika yang nyaman digunakan. Dalam contoh berikut, kami mengonversi frekuensi triwulanan dengan tahun yang berakhir pada bulan November menjadi pukul 9 pagi pada akhir bulan setelah akhir kuartal:
```py
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")

ts = pd.Series(np.random.randn(len(prng)), prng)

ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9

ts.head()
```

</br>

## Categoricals
---
pandas dapat menyertakan data kategorikal dalam file DataFrame.
```py
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
```
Mengonversi nilai mentah menjadi tipe data kategoris:
```py
df["grade"] = df["raw_grade"].astype("category")

df["grade"]
```
Ganti nama kategori menjadi nama yang lebih bermakna (penugasan ke `Series.cat.categories()` sudah ada!):
```py
df["grade"].cat.categories = ["very good", "good", "very bad"]
```
Susun ulang kategori dan tambahkan kategori yang hilang secara bersamaan (metode di bawah `Series.cat()` mengembalikan yang baru Seriessecara default):
```py
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)


df["grade"]
```
Penyortiran adalah per urutan dalam kategori, bukan urutan leksikal:
```py
df.sort_values(by="grade")
```
Pengelompokan menurut kolom kategoris juga menunjukkan kategori kosong:
```py
df.groupby("grade").size()
```

</br>

## Plotting
---
Menggunakan konvensi standar untuk mereferensikan matplotlib API:
```py
import matplotlib.pyplot as plt

plt.close("all")
```
Metode `close()` ini digunakan untuk menutup jendela gambar:
```py
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

ts.plot();
```
Jika berjalan di bawah Jupyter Notebook, plot akan muncul di plot(). Jika tidak, gunakan `matplotlib.pyplot.show` untuk menampilkannya atau `matplotlib.pyplot.savefig` untuk menulisnya ke file.
```py
plt.show();
```
Pada DataFrame, plot() metode ini memudahkan untuk memplot semua kolom dengan label:
```py
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)


df = df.cumsum()

plt.figure();

df.plot();

plt.legend(loc='best');
```

</br>

## Getting data in/out
---
### CSV
Menulis ke file csv:
```py
df.to_csv("foo.csv")
```
Membaca dari file csv:
```py
pd.read_csv("foo.csv")
```
### HDF5
Menulis ke Store HDF5:
```py
df.to_hdf("foo.h5", "df")
```
Membaca dari Store HDF5:
```py
pd.read_hdf("foo.h5", "df")
```
### Excel
Menulis ke file excel:
```py
df.to_excel("foo.xlsx", sheet_name="Sheet1")
```
Membaca dari file excel:
```py
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
```

</br>

## Gotchas
---
Jika Anda mencoba melakukan operasi, Anda mungkin melihat pengecualian seperti:
```py
if pd.Series([False, True, False]):
    print("I was true")
```