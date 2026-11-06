import random
class Karty:
    def __init__(self):
        self.karty = []
        self.talia=[]
    def pick(self,wybur):
        self.karty[wybur+1].uzyj()
    def check(self):
        for i in self.karty:
            print(i)
    def draw(self):
        while len(self.karty) < 4:
            x = random.randint(0,len(self.talia)-1)
            self.karty.append(self.talia[x])
            self.talia.remove(self.talia[x])

class Karta:
    def __init__(self,znaczek,wartosc):
        self.wartosc = wartosc
        self.znaczek = znaczek
    def pokaz(self):
        return f"{self.znaczek} {self.wartosc}"
    def uzyj(self):
        if self.znaczek=='♥':
            if gracz < 20:
                gracz + self.wartosc
                if gracz>20:
                    gracz = 20
            elif gracz >= 20:
                return ""
        elif self.znaczek == '♦':
            bron=self.wartosc
            killlist.clear()
        elif self.znaczek == '♣' or self.znaczek == '♠':
            if self.wartosc < killlist[-1] or len(killlist) == 0:
                x = self.wartosc - bron
                if x < 0:
                    x=0
                gracz -= x

test = Karty()
for i in range(1,14):
    test.talia.append(f"♥{i}")
for i in range(1,14):
    test.talia.append(f"♦{i}")
for i in range(1,14):
    test.talia.append(f"♣{i}")
for i in range(1,14):
    test.talia.append(f"♠{i}")
bron=0
killlist=[]
gracz=20

