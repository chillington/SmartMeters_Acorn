import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd

df = pd.read_csv('acorn_details.csv')

df2 = df.loc[df['CATEGORIES'] == 'Geography']
names = list(df2)

data = pd.melt(df2, id_vars=names[0:4], value_vars=names[4:22], var_name='Acorn Category', value_name='Acorn Index')

data['UK BASE'] = pd.to_numeric(data['UK BASE'], errors='coerce')
data['Acorn Index'] = pd.to_numeric(data['Acorn Index'], errors='coerce')
data.rename(columns={'REFERNCE': 'Country'}, inplace=True)

data2 = data.pivot(index='Acorn Category', columns='Country', values='Acorn Index')

data2.plot.bar()

plt.ylabel('Acorn Index')
plt.title("Representation of Acorn categories in each country\n-Index is relative to percentage of sample")

plt.tight_layout()
plt.show()
