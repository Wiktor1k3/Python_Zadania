a = {'Gazeta': 'szt', 'Pomidor': 'szt', 'Ryż': 'paczka', 'mleko': 'litr', 'Truskawki': 'kg'}
print(a)

c = {key: value for key, value in a.items() if value == 'szt'}
print(c)
