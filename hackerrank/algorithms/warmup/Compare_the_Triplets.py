a_arr = list(map(int, input().split(' ')))
b_arr = list(map(int, input().split(' ')))

a = 0
b = 0
for i in range(0, 3):
    if a_arr[i] > b_arr[i]: a += 1
    elif b_arr[i] > a_arr[i]: b += 1
    else: pass

print(str(a) + ' ' + str(b))