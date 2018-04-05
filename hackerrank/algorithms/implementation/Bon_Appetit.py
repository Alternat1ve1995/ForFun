l, k = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
n = int(input())
print((n - (int((sum(arr) - arr[k]) / 2)),'Bon Appetit')[n - ((sum(arr) - arr[k]) / 2) == 0])
