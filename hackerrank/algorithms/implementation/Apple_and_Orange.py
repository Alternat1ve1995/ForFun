class Map:

    def __init__(self, s, t, a, b):
        self.__s = s
        self.__t = t
        self. __a = a
        self.__b = b

    def isAplleScored(self, dst):
        fall = self.__a + dst
        if fall >= self.__s and fall <= self.__t: return 1
        return 0

    def isOrangeScored(self, dst):
        fall = self.__b + dst
        if fall >= self.__s and fall <= self.__t: return 1
        return 0


st = list(map(int, input().split(' ')))
ab = list(map(int, input().split(' ')))
field = Map(st[0], st[1], ab[0], ab[1])
input()
apples_scored = 0
oranges_scored = 0

arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))

for sc in arr1: apples_scored += field.isAplleScored(sc)
for sc in arr2: oranges_scored += field.isOrangeScored(sc)

print(apples_scored)
print(oranges_scored)