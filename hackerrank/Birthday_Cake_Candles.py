input()
arr = list(map(int, input().split(' ')))
res = 0
arr.sort(reverse=True)
for i in range(0, len(arr)):
    if arr[i] != arr[0]: break
    res += 1

print(res)