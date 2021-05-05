import pandas as pd

# Zadanie1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

df=pd.read_excel('imiona.xlsx',index_col=0)
print(df)