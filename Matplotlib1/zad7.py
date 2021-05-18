import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('zamowienia.csv', header=0, sep=';')
a = df.groupby(['Sprzedawca']).Utarg.sum().reset_index()
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(a.Utarg,labels=a.Sprzedawca, autopct=lambda pct:'{:.2f}%'.format(pct),explode=explode,shadow=True)

plt.show()