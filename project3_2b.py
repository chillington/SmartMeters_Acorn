import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd

df = pd.read_csv('block_1.csv', header=0, names=['LCLid','DateTime','KWH_hh'], parse_dates=[1])

df['KWH_hh'] = pd.to_numeric(df['KWH_hh'], errors='coerce')

temp = pd.DatetimeIndex(df['DateTime'])
df['Date'] = temp.date
df['Time'] = temp.time
del df['DateTime']

df['Date'] = pd.to_datetime(df['Date'])

inf = pd.read_csv('~/dssa5001/week11/informations_household_update.csv')

inf2 = inf.loc[inf['Acorn_grouped'] == 'Adversity']

ids = []
ids = inf2['LCLid']

data = df.loc[df['LCLid'].isin(ids)]

df2 = data.groupby(['Date', 'LCLid'])['KWH_hh'].mean().reset_index()

data2 = df2.pivot(index='Date', columns='LCLid', values='KWH_hh').fillna(0)

ax = data2.plot()

ax.set_title("Daily energy usage (Mean KWH per half hour)\nin Block 1 ""Adversity"" households\n11/23/2011-2/28/2014")
ax.set_xlabel('Date')
ax.set_ylabel('Daily mean KWH per half hour')
ax.text(15500,2.5,"Each line represents one household")
ax.legend_.remove()
plt.show()
