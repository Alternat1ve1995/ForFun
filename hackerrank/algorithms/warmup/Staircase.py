size = int(input())

for i in range(0, size):
    for k in range(0, size - i - 1): print(' ', end='')
    for p in range(0, i + 1): print('#', end='')
    print()
