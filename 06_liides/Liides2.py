from abc import ABC, abstractmethod
import datetime

class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass

    @abstractmethod
    def getSum(self) -> float:
        pass

class simpleAdder(Adder):
    def __init__(self):
        self.total = 0
    
    def add(self, nr: float) -> None:
        self.total += nr

    def getSum(self) -> float:
        return self.total
    
class FileStoringAdder(Adder):
    def __init__(self, failinimi):
        self.failinimi = failinimi
        
    def add(self, nr: float) -> None:
        with open(self.failinimi, "a") as f2:
            print(nr, datetime.datetime.now().strftime("%X"), sep =",", file=f2)

    def getSum(self):
        return sum(
            float(rida.split(",")[0])
            for rida in open(self.failinimi)
            if rida.strip())
    
class charCounter:
    def __init__(self, a: Adder):
        self.adder = a
        self.wordadder = None

    def setWordAdder(self, a2: Adder):
        self.wordadder = a2

    def addWordCharacters(self, word):
        self.adder.add(len(word))
        if self.wordadder:
            self.wordadder.add(1)

    def getCharacterCount(self):
        return self.adder.getSum()
    
    def getWordCount(self):
        if self.wordadder:
            return self.wordadder.getSum()
        return - 1
    
class CharCounter:
    def __init__(self, a: Adder):
        self.adder=a
    
    def addWordCharacters(self, word):
        self.adder.add(len(word))
    
    def getCharacterCount(self):
        return self.adder.getSum()
    
sa = simpleAdder()
sa.add(3)
sa.add(2)
print(sa.getSum())

sa2 = simpleAdder()
lugeja1 = charCounter(sa)
lugeja1.setWordAdder(sa2)
lugeja1.addWordCharacters("Juku")
lugeja1.addWordCharacters("Kati")
print(lugeja1.getCharacterCount())
print(lugeja1.getWordCount())
a:Adder = FileStoringAdder("arvud1.txt")
a.add(7)
a.add(11)
c:CharCounter(a)
sisend=input("Palun lause, katkestuseks enter: ")
print(a.getSum())