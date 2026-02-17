import random

class Korvpallur:
    
    def __init__(self, nimi, visketapsus):
        self.nimi = nimi
        self.visketapsus = visketapsus
        self.punktid = 0

    def viska_kahene(self):
        vise = random.randint(1, 100)
        if vise <= self.visketapsus:
            self.punktid += 2
            print(self.nimi, "Kahene sees! 2 punkti juurde")
        else:
            print(self.nimi, "Kahene mööda.")

    def viska_kolmene(self):
        vise = random.randint(1, 100)
        if vise <= self.visketapsus - 15:
            self.punktid += 3
            print(self.nimi, "Kolmene sees! 3 punkti juurde")
        else:
            print(self.nimi, "mööda kolmene.")

    def info(self):
        return self.nimi + ": " + str(self.punktid) + " punkti"

    def __str__(self):
        return self.info()

m1 = Korvpallur("LeBron James", 70)
m2 = Korvpallur("Stephen Curry", 85)

print("Algab viskevõistlus!\n")

for i in range(5):
    print("Voor", i + 1)
    
    m1.viska_kahene()
    m2.viska_kahene()
    
    m1.viska_kolmene()
    m2.viska_kolmene()
    
    print()

print("Lõpptulemused:")
print(m1)
print(m2)

if m1.punktid > m2.punktid:
    print("Võitis:", m1.nimi)
elif m2.punktid > m1.punktid:
    print("Võitis:", m2.nimi)
else:
    print("Viik!")
