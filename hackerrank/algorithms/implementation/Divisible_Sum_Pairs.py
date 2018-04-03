def amount_of_pairs_for_index(index):
    global amount
    for i in range(index + 1, l):
        if (arr[i] + arr[index]) % k == 0: amount += 1

amount = 0
l, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i, j in enumerate(arr): amount_of_pairs_for_index(i)

print(amount)
