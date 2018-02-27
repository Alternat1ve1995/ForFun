def grade(gr): return (gr ,gr + 5 -(gr % 5))[gr % 5 > 2 and gr > 37]
input()

data = []
while True:
    try: data.append(int(input()))
    except: break

for gr in data: print(grade(gr))
