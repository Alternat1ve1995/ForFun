import sys

def migratoryBirds(n, ar):
    arr = [(lambda x: 0)(x) for x in range(0, 5)]
    for n in ar: arr[n - 1] += 1
    return arr.index(max(arr)) + 1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
