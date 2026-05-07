import itertools

class Tekst:
    def __init__(self, sisu: str, nimi: str = ""):
        self.sisu = sisu
        self.nimi = nimi

    @classmethod
    def from_file(cls, failitee: str) -> "Tekst":
        with open(failitee, encoding="utf-8") as f:
            return cls(f.read(), nimi=failitee)
        
    def symboli_osakaal(self, sümbol: str) -> float:
        if not self.sisu:
            return 0.0
        return round(self.sisu.count(sümbol) / len(self.sisu), 2)

    def erinevus(self, teine: "Tekst", tähed: list[str]) -> float:
        summa = sum(
            abs(self.symboli_osakaal(täht) - teine.symboli_osakaal(täht))
            for täht in tähed
        )
        return round(summa, 2)


def vordle_koiki(tekstid: list[Tekst], tähed: list[str]):
    paarid = list(itertools.combinations(tekstid, 2))
    tulemused = []
    for t1, t2 in paarid:
        er = t1.erinevus(t2, tähed)
        tulemused.append((t1, t2, er))

    keskmine = round(sum(er for _, _, er in tulemused) / len(tulemused), 2)

    print("Ülesanne 3:", f"Kõikide tekstipaaride erinevuste osakaalude summa keskmine: {keskmine}\n")
    def vota_erinevus(x):
        return x[2]
    
    tulemused.sort(key=vota_erinevus)
    for t1, t2, er in tulemused:
        print(f"{t1.nimi} — {t2.nimi}: {er}")

tekstid = [
    Tekst.from_file("tekst1.txt"),
    Tekst.from_file("tekst2.txt"),
    Tekst.from_file("tekst3.txt"),
    Tekst.from_file("tekst4.txt"),
    Tekst.from_file("tekst5.txt"),
    Tekst.from_file("tekst6.txt"),
    Tekst.from_file("tekst7.txt"),
    Tekst.from_file("tekst8.txt"),
]

print("Ülesanne 1:", tekstid[0].symboli_osakaal("a"))
print("Ülesanne 2:", tekstid[0].erinevus(tekstid[1], ["a", "b"]))

vordle_koiki(tekstid, ["a", "b"])