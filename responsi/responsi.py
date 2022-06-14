import requests

url = 'https://stats.govt.nz/assets/Uploads/Environmental-economic-accounts/Environmental-economic-accounts-data-to-2020/environmental-protection-expenditure-2009-2020-csv.csv'
r = requests.get(url, allow_redirects=True)

open('environmental.csv', 'wb').write(r.content)

import pandas as pd

data= pd.read_csv("environmental.csv")
data.head()