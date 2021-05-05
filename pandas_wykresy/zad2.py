import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')

grupa = a.groupby(["Plec"]).agg({'Liczba':['sum']})
wykres = grupa.plot.bar()
wykres.set_ylabel('Mld')
wykres.legend()
plt.xticks(rotation=0)
plt.title('Urodzone dzieci')
plt.show()



