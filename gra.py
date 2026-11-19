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
gracz=20
bron=0
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
    karty.talia.append(f'♥')
    karty.talia2.append({i})
for i in range(1,14):
    karty.talia.append(f'♦')
    karty.talia2.append({i})
for i in range(1,14):
    karty.talia.append(f'♣')
    karty.talia2.append({i})
for i in range(1,14):
    karty.talia.append(f'♠')
    karty.talia2.append({i})
killlist=[]
# karty.draw()
# print(karty.check())
while gracz > 0:
     print("wybierz opcje:")
     print("1. zobacz karty na stole")
     print("2. wybierz karte")
     print("3. zobacz stan broni")
     print("4. wyjdź")
     wybur = input("opcja: ")
     if gracz <= 0:
         print("Przegraleś!")
         break
     if wybur == "1":
        karty.draw()
        print(karty.check())
     elif wybur == "4":
         break
     elif wybur == "3":
        print("Stan broni:",bron)
     elif wybur == "2":
         karty.draw()
         print(karty.check())
         w = input("Wybierz kartę:")
         if w == "1":
            print(karty.karty[0].pokaz())
            if karty.karty[0].znaczek=='♥':
                        if gracz < 20:
                            gracz + karty.karty[0].wartosc
                            if gracz>20:
                                gracz = 20
                        elif gracz >= 20:
                            print("")
            elif karty.karty[0].znaczek == '♦':
                bron=karty.karty[0].wartosc
                killlist.clear()
            elif karty.karty[0].znaczek == '♣' or karty.karty[0].znaczek == '♠':
                if karty.karty[0].wartosc < killlist[-1] or len(killlist) == 0:
                        x = karty.karty[0].wartosc - bron
                        if x < 0:
                            x=0
                        gracz -= x
            karty.karty.pop(0)
         if w == "2":
            print(karty.karty[1].pokaz())
            if karty.karty[1].znaczek=='♥':
                if gracz < 20:
                    gracz + karty.karty[1].wartosc
                    if gracz>20:
                        gracz = 20
                    elif gracz >= 20:
                        print("")
            elif karty.karty[1].znaczek == '♦':
                    bron=karty.karty[1].wartosc
                    killlist.clear()
            elif karty.karty[1].znaczek == '♣' or karty.karty[1].znaczek == '♠':
                    if karty.karty[1].wartosc < killlist[-1] or len(killlist) == 0:
                        x = karty.karty[1].wartosc - bron
                        if x < 0:
                            x=0
                        gracz -= x
            karty.karty.pop(1)
         if w == "3":
            print(karty.karty[2].pokaz())
            karty.karty[2].uzyj()
            if karty.karty[2].znaczek=='♥':
                if gracz < 20:
                    gracz + karty.karty[2].wartosc
                    if gracz>20:
                        gracz = 20
                    elif gracz >= 20:
                        print("")
            elif karty.karty[2].znaczek == '♦':
                bron=karty.karty[2].wartosc
                killlist.clear()
            elif karty.karty[2].znaczek == '♣' or karty.karty[2].znaczek == '♠':
                if karty.karty[2].wartosc < killlist[-1] or len(killlist) == 0:
                    x = karty.karty[2].wartosc - bron
                    if x < 0:
                        x=0
                    gracz -= x
            karty.karty.pop(2)
         if w == "4":
            print(karty.karty[3].pokaz())
                        
            if karty.karty[3].znaczek=='♥':
                if gracz < 20:
                    gracz + karty.karty[3].wartosc
                    if gracz>20:
                        gracz = 20
                elif gracz >= 20:
                    print("")
            elif karty.karty[3].znaczek == '♦':
                bron=karty.karty[3].wartosc
                killlist.clear()
            elif karty.karty[3].znaczek == '♣' or karty.karty[3].znaczek == '♠':
                if karty.karty[3].wartosc < killlist[-1] or len(killlist) == 0:
                    x = karty.karty[3].wartosc - bron
                    if x < 0:
                        x=0
                    gracz -= x
            karty.karty.pop(3)
