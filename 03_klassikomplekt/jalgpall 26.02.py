import random

class Jalgpallur:

    def __init__(self, nimi, tapsus):
        self.nimi = nimi
        self.tapsus = tapsus
        self.varavad = 0

    def penalti(self):
        look = random.randint(1, 100)
        if self.tapsus * 0.8 >= look:
            self.varavad += 1
            print(self.nimi, "lõi penalti sisse!")
        else:
            print(self.nimi, "eksis penaltil.")

    def __str__(self):
        return self.nimi + ": " + str(self.varavad) + " väravat"


class Mang:

    def __init__(self, jalgpallur1, jalgpallur2):
        self.m1 = jalgpallur1
        self.m2 = jalgpallur2

    def alusta(self, voorud=3):
        for i in range(voorud):
            print("Voor", i + 1)
            self.m1.penalti()
            self.m2.penalti()
            print()

        print("Lõpptulemused:")
        print(self.m1)
        print(self.m2)

        if self.m1.varavad > self.m2.varavad:
            print("Võitis:", self.m1.nimi)
        elif self.m2.varavad > self.m1.varavad:
            print("Võitis:", self.m2.nimi)
        else:
            print("Viik!")

m1 = Jalgpallur("Gyökeres", 92)
m2 = Jalgpallur("Palmer", 87)

mang = Mang(m1, m2)
mang.alusta(3)