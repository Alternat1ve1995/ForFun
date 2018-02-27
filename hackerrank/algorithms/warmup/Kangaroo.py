class Kangaroo:
    def __init__(self, start, speed):
        self.pos = start
        self.speed = speed

    def jump(self): self.pos += self.speed

    def canOvertake(self, kangaroo): return (False, True)[self.pos <= kangaroo.pos and self.speed > kangaroo.speed]

data = list(map(int, input().split(' ')))
kangaroo1 = Kangaroo(data[0], data[1])
kangaroo2 = Kangaroo(data[2], data[3])

while kangaroo1.canOvertake(kangaroo2) or kangaroo2.canOvertake(kangaroo1):
    if kangaroo1.pos == kangaroo2.pos:
        print('YES')
        break
    else:
        kangaroo1.jump()
        kangaroo2.jump()

if kangaroo1.pos != kangaroo2.pos: print('NO')
