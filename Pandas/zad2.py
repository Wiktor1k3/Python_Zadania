import pandas as pd

df=pd.read_excel('imiona.xlsx')

# Zadanie 2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

# a) tylko te rekordy gdzie liczba nadanych imion była mniejsza niż 1000 w danym roku

print(df[df['Liczba']<1000])

# b) tylko rekordy gdzie nadane imię jest takie jak Twoje

print(df[df['Imie']=='WIKTOR'])

# c) sumę wszystkich urodzonych dzieci w całym danym okresie,

print("C)Suma wszystkich dzieci:"),print( df['Liczba'].sum())

# d) sumę dzieci urodzonych w latach 2005-2010

a=(df[( df.Rok > 2005 ) & ( df.Rok < 2010 )])
print("D)Suma dzieci urodzonych w latach 2005-2010:"),print(a['Liczba'].sum())

# e) sumę urodzonych chłopców w 2000 roku

b=(df[(2000 == df.Rok) & (df.Plec == 'M')])
print("E)Suma urodzonych chłopców w 2000 roku:")
print(b["Liczba"].sum())

# f) najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)

print("F)Najbardziej popularne imię dziewczynki i chłopca w danym roku:")

male= df[df.Plec == 'M']
female= df[df.Plec == 'K']

x = male.loc[male.groupby('Rok')['Liczba'].idxmax()]
y = female.loc[female.groupby('Rok')['Liczba'].idxmax()]
print(x[['Rok', 'Imie']])
print(y[['Rok', 'Imie']])

# g) najbardziej popularne imię dziewczynki i chłopca w całym danym okresie

popMale = male.loc[male['Liczba'].idxmax()]
popFemale = female.loc[female['Liczba'].idxmax()]

print('G)Najbardziej popularne imię dziewczynki i chłopca w całym danym okresie:')
print(popMale.Imie, popFemale.Imie)
