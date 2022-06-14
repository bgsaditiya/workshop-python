# Responsi Workshop Python

</br>

## Mengunduh file menggunakan python
---
Import modul `requests`:
```py
import requests
```
Dapatkan tautan atau url:
```py
url = 'https://stats.govt.nz/assets/Uploads/Environmental-economic-accounts/Environmental-economic-accounts-data-to-2020/environmental-protection-expenditure-2009-2020-csv.csv'
r = requests.get(url, allow_redirects=True)
```
Simpan file dengan nama `environmental.csv`:
```py
open('environmental.csv', 'wb').write(r.content)
```

</br>

## Menampilkan sebagian file csv
---
Import modul pandas:
```py
import pandas as pd
```
Memuat file `environmental.csv` menggunakan fungsi `read_csv()`:
```py
data= pd.read_csv("environmental.csv")
data.head()
```
Fungsi `.head(n)` akan menampilkan 5 baris data teratas, jika parameter n tidak diisi.