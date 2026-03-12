from abc import ABC, abstractmethod
from datetime import datetime

class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass

    @abstractmethod
    def getSum(self) -> float:
        pass
    
class HoldingAdder(ABC):
    @abstractmethod
    def add(self, nr:float) -> None:
        pass

class simpleAdder(Adder):
    def __init__(self):
        self.total = 0
    
    def add(self, nr: float) -> None:
        self.total += nr

    def getSum(self) -> float:
        return self.total
    
class FileAdder(Adder):
    def __init__(self, filename: str):
        self.filename = filename
        
    def add(self, nr: float) -> None:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"{nr},{now}\n")
            
    def getSum(self) -> float:
        total = 0
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    total += float(parts[0])
        except FileNotFoundError:
            return 0
        return total
    
    def getEntryCount(self) -> int:
        count = 0
        try:
            with open(self.filename, "r") as f:
                for _ in f:
                    count += 1
                except FileNotFoundError:
                    return 0
                return count
    
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