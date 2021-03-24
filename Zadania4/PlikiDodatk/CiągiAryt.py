class CiągiAryt:
    a1 = 0
    roznica = 0
    ilosc = 0
    elCiagu = [a1]

    def wyświetl_dane(self):
        print(self.elCiagu)
    def pobierz_elementy(self, *n):
        pobraneElementy = []
        for x in n:
            pobraneElementy.append(self.elCiagu[x - 1])
        print(pobraneElementy)

    def pobierz_parametry(self, a1, roznica, ilosc):
        self.a1 = a1
        self.roznica = roznica
        self.ilosc = ilosc

    def policz_sume(self):

        suma = 0
        for x in self.elCiagu:
            suma += x
        print(suma)

    def policz_elementy(self):
        if self.roznica != 0:
            a1 = self.a1
            for x in range(self.ilosc):
                an = a1 + self.roznica
                self.elCiagu.append(an)
                a1 = an