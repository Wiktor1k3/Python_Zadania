class NaZakupy:
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_Produkt(self):
        print(self.ilosc, self.nazwa_produktu, self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)

    def ile_kosztuje(self):
        kwota = self.ilosc * self.cena_jed
        return kwota