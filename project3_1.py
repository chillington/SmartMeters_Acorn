import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd

inf = pd.read_csv('informations_household_update.csv')

inf2 = inf.loc[inf['Acorn_grouped'].isin(['Affluent','Adversity','Comfortable'])]


df = inf2.groupby(['Acorn_grouped', 'file'])['LCLid'].count().unstack('Acorn_grouped').fillna(0)

df.plot.bar(stacked=True)

plt.ylabel('Number of households')

plt.xlabel('Block')

plt.title("Number of households in each block\nby ACORN classification group")

plt.legend(loc='upper center', ncol=3, fontsize='x-small')

plt.tight_layout()

plt.show()
