import math


def get_diag(matrix, natural=True):
    diag = []
    start = (len(matrix[0]) - 1, 0)[natural]
    end = (0, len(matrix[0]))[natural]
    for i in range(start, (-1, end)[natural], (-1, 1)[natural]):
        diag.append(matrix[i][(len(matrix[0]) - start - 1, i)[natural]])
    return diag

input()
matrix = []
while True:
    try: arr = list(map(int, input().split(' ')))
    except EOFError:break
    if arr is not None:
        matrix.append(arr)
    else: break

diag1 = get_diag(matrix)
diag2 = get_diag(matrix, False)
sum1 = 0
sum2 = 0

for i in range(0, len(diag1)):
    sum1 += diag1[i]
    sum2 += diag2[i]

print(math.fabs(sum1 - sum2))
