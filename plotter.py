import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 16
fig_size[1] = 9
plt.rc('xtick',labelsize=8)
plt.rcParams["figure.figsize"] = fig_size
books_data = pd.read_csv('books.csv')
averaged = books_data.groupby('Category').mean()
averaged.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Average Price")

plt.savefig('averages.png',dpi=300)

