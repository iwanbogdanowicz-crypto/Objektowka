import random
class Karty:
    def __init__(self):
        self.karty = []
        self.talia=[]
        self.talia2=[]
    def pick(self,wybur):
        self.karty[wybur+1].uzyj()
    def check(self):
        for i in self.karty:
            print(i.pokaz())
    def draw(self):
        while len(self.karty) < 4:
            x = random.randint(0,round(len(self.talia)/2))
            y = random.randint(0,round(len(self.talia2)/2))
            self.karty.append(Karta(self.talia[x],self.talia2[y]))
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
karty = Karty()
for i in range(1,14):
    karty.talia.append(f"♥")
    karty.talia2.append({i})
for i in range(1,14):
    karty.talia.append(f"♦")
    karty.talia2.append({i})
for i in range(1,14):
    karty.talia.append(f"♣")
    karty.talia2.append({i})
for i in range(1,14):
    karty.talia.append(f"♠")
    karty.talia2.append({i})
bron=0
killlist=[]
gracz=20
# karty.draw()
# print(karty.check())
while gracz > 0:
     print("wybierz opcje:")
     print("1. zobacz karty na stole")
     print("2. wybierz karte")
     print("3. zobacz stan broni")
     print("4. wyjdź bo masz skill issue :3")
     wybur = input("opcja: ")
     if wybur == "1":
        karty.draw()
        print(karty.check())
     elif wybur == "4":
         break
     elif wybur == "3":
        print("Stan broni:",bron)
    
