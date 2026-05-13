class Mangija:
    def __init__(self, nimi, number, klubi):
        self.nimi = nimi
        self.number = number
        self.klubi = klubi
        self._on_valjakul = False

    def tule_valjakule(self):
        self._on_valjakul = True
        print(f"{self.nimi} tuleb väljakule.")

    def lahku_valjakult(self):
        self._on_valjakul = False
        print(f"{self.nimi} lahkub väljakult.")

    def __str__(self):
        return f"{self.nimi} | #{self.number} | {self.klubi}"


class Valjakumangija(Mangija):
    def __init__(self, nimi, number, klubi, soodud):
        super().__init__(nimi, number, klubi)
        self.soodud = soodud

    def sooda(self, kellele):
        if self._on_valjakul:
            print(f"{self.nimi} söödab → {kellele}")
        else:
            print(f"Viga: {self.nimi} ei ole väljakul!")

    def __str__(self):
        return super().__str__() + f" | söödud: {self.soodud}"


class Rundaja(Valjakumangija):
    def __init__(self, nimi, number, klubi, soodud, varavad):
        super().__init__(nimi, number, klubi, soodud)
        self.varavad = varavad

    def loo_varav(self):
        if self._on_valjakul:
            self.varavad += 1
            print(f"{self.nimi} lööb värava! Kokku: {self.varavad}")
        else:
            print(f"Viga: {self.nimi} ei ole väljakul!")

    def __str__(self):
        return super().__str__() + f" | väravad: {self.varavad}"


class Kaitsja(Valjakumangija):
    def __init__(self, nimi, number, klubi, soodud, blokeeringud):
        super().__init__(nimi, number, klubi, soodud)
        self.blokeeringud = blokeeringud

    def blokeeri(self):
        if self._on_valjakul:
            self.blokeeringud += 1
            print(f"{self.nimi} blokeerib! Kokku: {self.blokeeringud}")
        else:
            print(f"Viga: {self.nimi} ei ole väljakul!")

    def __str__(self):
        return super().__str__() + f" | Blokeeringud: {self.blokeeringud}"


if __name__ == "__main__":
    rundaja = Rundaja("Saka", 7, "Arsenal", 5, 0)
    kaitsja = Kaitsja("Saliba", 2, "Arsenal", 12, 0)

    print(rundaja)
    print(kaitsja)
    print("")
    rundaja.loo_varav()
    rundaja.tule_valjakule()
    kaitsja.tule_valjakule()
    rundaja.sooda("Trossard")
    rundaja.loo_varav()
    kaitsja.blokeeri()
    rundaja.lahku_valjakult()