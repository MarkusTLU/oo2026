def KaksKeskmist(v1: float, v2: float) -> float:
    return round(2 * v1 * v2 / (v1 + v2), 2)

def KMKeskmised(kiirused: list[float]) -> float:
    n = len(kiirused)
    return round(n / sum(1/v for v in kiirused), 2)

class Teekond:
    def __init__(self):
        self.kiirused = []

    def lisa_loik(self, kiirus: float):
        self.kiirused.append(kiirus)

    def kuva_asukohad(self):
        print("Ülesanne 3: ")

        asukoht = 0.0
        minut = 0

        for loik_nr, kiirus in enumerate(self.kiirused):
            minuteid_loigus = 60 / kiirus
            kulunud = 0.0
            
            while kulunud + 1 <= minuteid_loigus:
                kulunud += 1
                minut += 1
                asukoht = loik_nr + kulunud / minuteid_loigus
                print(f"{minut:<10} {asukoht:<15.2f}")

print("Ülesanne 1: ", KaksKeskmist(30, 60))
print("Ülesanne 2: ", KMKeskmised([80, 100, 120, 140]))

teekond = Teekond()
teekond.lisa_loik(20)
teekond.lisa_loik(30)
teekond.lisa_loik(40)

teekond.kuva_asukohad()