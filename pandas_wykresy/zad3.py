import pandas as pd
import matplotlib.pyplot as plt


a = pd.read_excel('imiona.xlsx')
b = a[(a['Rok'] >= 2012)]
grupa = b.groupby(["Plec"]).agg({'Liczba': ['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=12, figsize=(6, 6))
plt.legend(loc='lower right')
plt.show()