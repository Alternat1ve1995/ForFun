input()
arr = list(map(int, input().split(' ')))

zero = list(x for x in arr if x == 0)
pos = list(x for x in arr if x > 0)
neg = list(x for x in arr if x < 0)

print("%.6f" % (len(pos) / len(arr)))
print("%.6f" % (len(neg) / len(arr)))
print("%.6f" % (len(zero) / len(arr)))
