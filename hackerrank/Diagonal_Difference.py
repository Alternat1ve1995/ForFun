import math


def get_diag(matrix, natural=True):
    diag = []
    start = ([0, len(matrix[0]) - 1], [0, 0])[natural]
    end = ([len(matrix), -1], [len(matrix), len(matrix[0])])[natural]

    for i, j in list(zip(range(start[0], end[0]), range(start[1], end[1], (-1, 1)[natural]))): diag.append(matrix[i][j])
    return diag

input()
matrix = []
while True:
    try: arr = list(map(int, input().split(' ')))
    except EOFError: break
    matrix.append(arr)


res = 0
for i, j in list(zip(get_diag(matrix), get_diag(matrix, False))): res += (i - j)

print(int(math.fabs(res)))
