def amount_of_pairs_for_index(index):
    global amount
    for i in range(index + 1, len(arr)):
        if (arr[i] + arr[index]) % k == 0: amount += 1

amount = 0
k = list(map(int, input().split()))[1]
arr = list(map(int, input().split()))

for i, j in enumerate(arr): amount_of_pairs_for_index(i)

print(amount)
