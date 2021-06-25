# env: Google Colab
ans = [1849, 272400, 35]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from google.colab import auth

auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default()) 
worksheet = gc.open_by_url('***').sheet1

rows = worksheet.get_all_values() 
print(rows)

for e in rows[1:]:
  for i in range(len(e)):
    if i < 2: continue
    e[i] = str(abs(int(e[i])-ans[i-2]))

df = pd.DataFrame.from_records(rows[1:], columns=range(5))
df = df.drop(0, axis=1)
df = df.drop(1, axis=1)
display(df)

df.to_csv('ds.csv')
