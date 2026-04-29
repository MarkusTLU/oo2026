import sys
sys.stdout.reconfigure(encoding='utf-8')
from abc import ABC, abstractmethod

class Varavaloendaja(ABC):
    @abstractmethod
    def lisa_varav(self, mangija: str) -> None:
        pass

    @abstractmethod
    def get_varavad(self) -> dict[str, int]:
        pass

    @abstractmethod
    def suurim_looja(self) -> str:
        pass

    @abstractmethod
    def salvesta_faili(self, failinimi: str) -> None:
        pass

class ManguLoendaja(Varavaloendaja):
    def __init__(self):
        self._varavad: dict[str, int] = {}

    def lisa_varav(self, mangija: str) -> None:
        self._varavad[mangija] = self._varavad.get(mangija, 0) + 1

    def get_varavad(self) -> dict[str, int]:
        return dict(self._varavad)

    def suurim_looja(self) -> str:
        if not self._varavad:
            return "Väravaid pole veel löödud"
        parim = max(self._varavad, key=lambda m: self._varavad[m])
        return f"{parim} ({self._varavad[parim]} väravat)"

    def salvesta_faili(self, failinimi: str) -> None:
        with open(failinimi, "w", encoding="utf-8") as f:
            f.write("Väravad mängijate kaupa:\n")
            for mangija, arv in self._varavad.items():
                f.write(f"  {mangija}: {arv}\n")
            f.write(f"\nSuurim väravatelööja: {self.suurim_looja()}\n")

loendaja = ManguLoendaja()
loendaja.lisa_varav("Saka")
loendaja.lisa_varav("Martinelli")
loendaja.lisa_varav("Saka")
loendaja.lisa_varav("Jesus")
loendaja.lisa_varav("Saka")
loendaja.lisa_varav("Martinelli")

print("Väravad mängijate kaupa:")
for mangija, arv in loendaja.get_varavad().items():
    print(f"  {mangija}: {arv}")

print(f"\nSuurim väravatelööja: {loendaja.suurim_looja()}")

loendaja.salvesta_faili("tulemused.txt")
print("\nTulemused salvestatud faili tulemused.txt")