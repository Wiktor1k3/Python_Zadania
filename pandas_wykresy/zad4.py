import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
grupa = a.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})

wykres = grupa.plot.bar()
plt.show()