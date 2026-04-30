import math
from PIL import Image, ImageDraw
import tkinter as tk

class Hulknurk:
    def __init__(self, cx, cy, r, n):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.n = n
        
    def tipu_koordinaadid(self):
        tipud = []
        for i in range(self.n):
            nurk = 2 * math.pi * i / self.n
            x = round(self.cx + self.r * math.cos(nurk), 2)
            y = round(self.cy + self.r * math.sin(nurk), 2)
            tipud.append((x, y))
        return tipud
    
    def pindala(self):
        return round((self.n * self.r**2 * math.sin(2 * math.pi / self.n)) / 2, 2)
    
    def joonista(self):
        img = Image.new("RGB", (400, 400), "white")
        draw = ImageDraw.Draw(img)
        draw.polygon(self.tipu_koordinaadid(), outline="black")
        return img
        
from PIL import ImageTk

def uuenda(event=None):
    n = slider.get()
    h = Hulknurk(200, 200, 100, n)

    img = h.joonista()
    img.save("hulknurk.png")

    photo = ImageTk.PhotoImage(img)
    canvas.config(image=photo)
    canvas.image = photo

    pindala_tekst.config(text=f"Pindala: {h.pindala()} px²")

aken = tk.Tk()
aken.title("Hulknurk")

slider = tk.Scale(aken, from_=3, to=12, orient="horizontal", label="Tippude arv", command=uuenda)
slider.pack()

canvas = tk.Label(aken)
canvas.pack()

pindala_tekst = tk.Label(aken, text="Pindala: ")
pindala_tekst.pack()

uuenda()
aken.mainloop()