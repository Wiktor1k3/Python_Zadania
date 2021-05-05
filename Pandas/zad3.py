import pandas as pd

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')

# Lista unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
df1 = df.Sprzedawca
df1 = df1.drop_duplicates()
print(df1)

# 5 najwyższych wartości zamówień
df2 = df
df2.Utarg = df2.Utarg.astype(float)
df2 = df2.sort_values(by='Utarg', ascending=False)
print("5 najwyższych wartości zamówień:")
print(df2['Utarg'].head(5))

# Ilość zamówień złożonych przez każdego sprzedawcę
print(df.groupby(['Sprzedawca']).agg({'Sprzedawca': ['count']}))

# Suma zamówień dla każdego kraju
print(df.groupby(['Kraj']).agg({'idZamowienia': ['count']}))

# Suma zamówień dla roku 2005, dla sprzedawców z Polski
df5 = df[(df['Kraj'] == "Polska")]
df5 = df5[(df5['Data zamowienia'] >= '2005-01-01') & (df5['Data zamowienia'] <= '2005-12-31')]
print(df5)

# Średnia kwota zamówienia w 2004 roku,

df6 = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')]
df6 = df6.Utarg
print('Średnia kwota zamówienia w 2004 roku:')
print(df6.mean())

# Zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
a = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')]
b = df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')]
a.to_csv('zamówienia_2004.csv', sep=';',index=0)
b.to_csv('zamówienia_2005.csv', sep=';',index=0)