input()
arr = list(map(int, input().split(' ')))
d, m = list(map(int, input().split(' ')))
res = 0
for i in range(m - 1, len(arr)): res += (0, 1)[sum(arr[(i - m + 1):i + 1]) == d]
print(res)
