import math
import matplotlib.pyplot as plt

class Hulknurk:
    xid = []
    yid = []
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.xid = [x1, x2, x3]
        self.yid = [y1, y2, y3]
        
    def lisa(self, x, y):
        self.xid.append(x)
        self.yid.append(y)
        print("Punkt lisatud:", (x, y))
        print("Uus ümbermõõt:", self.ymbermoot())
        
    def ymbermoot(self):
        p = 0
        n = len(self.xid)
        for i in range(len(self.xid)):
            dx = self.xid[(i + 1) % len(self.xid)] - self.xid[i]
            dy = self.yid[(i + 1) % len(self.yid)] - self.yid[i]
            p+=math.sqrt(dx*dx+dy*dy)
        return round(p, 2)
        
    def __str__(self):
        return ", ".join(["("+str(paar[0])+", "+str(paar[1])+")" for paar in zip(self.xid, self.yid)])
    
    def tekstiks(self):
        vastus=""
        for nr in range(3):
            vastus+=" ("+str(self.xid[nr])+", "+str(self.yid[nr])+")"
        return vastus
    
    def nihuta(self, dx, dy):
        self.xid = [x + dx for x in self.xid]
        self.yid = [y + dy for y in self.yid]
        print(f"Hulknurk nihutatud ({dx}, {dy}) võrra")
        
    def skaala(self, faktor):
        cx = sum(self.xid) / len(self.xid)
        cy = sum(self.yid) / len(self.yid)
        self.xid = [cx + (x - cx) * faktor for x in self.xid]
        self.yid = [cy + (y - cy) * faktor for y in self.yid]
        print(f"Hulknurk skaleeritud {faktor}")
        
    def kyljed(self):
        n = len(self.xid)
        kyljed = []
        for i in range(n):
            dx = self.xid[(i+1)%n] - self.xid[i]
            dy = self.yid[(i+1)%n] - self.yid[i]
            kyljed.append(round(math.sqrt(dx*dx + dy*dy), 2))
        return kyljed
    
    def koordinaadid(self):
        return list(zip(self.xid, self.yid))
    
    def kuva(self):
        x = self.xid + [self.xid[0]]
        y = self.yid + [self.yid[0]]
        plt.plot(x, y, marker='o')
        plt.fill(x, y, alpha=0.3)
        plt.title("Hulknurk")
        plt.grid(True)
        plt.show()
    
    
h1=Hulknurk(1, 3, 2, 4, 3, 5)
print(h1.xid, h1.yid)
h1.lisa(4, 7)
print("h1 pärast punkti lisamist:", h1)
h1.nihuta(2, 3)
print("Pärast nihutamist:", h1)
h1.skaala(4)
print("Pärast skaleerimist:", h1)
print("Külgede pikkused:", h1.kyljed())
print("Praegused koordinaadid:", h1.koordinaadid())
h1.kuva()
