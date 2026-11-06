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

test = Karty()


for i in range(1,14):
    test.talia.append(f"S{i}")
for i in range(1,14):
    test.talia.append(f"D{i}")
for i in range(1,14):
    test.talia.append(f"T{i}")
for i in range(1,14):
    test.talia.append(f"P{i}")

print(len(test.talia))
print(test.talia)
test.draw()
print(test.check())
