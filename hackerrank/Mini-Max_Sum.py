arr = list(map(int, input().split(' ')))
arr.sort()
print(str(sum(arr[:-1])) + ' ' + str(sum(arr[1:])))
