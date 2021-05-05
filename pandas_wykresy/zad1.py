import pandas as pd
import matplotlib.pyplot as plt


a = pd.read_excel('imiona.xlsx')
grupa = a.groupby(["Rok"]).agg({'Liczba': ['sum']})

wykres = grupa.cumsum()
print(wykres)
wykres.plot()
plt.ylabel('W mln')
plt.show()