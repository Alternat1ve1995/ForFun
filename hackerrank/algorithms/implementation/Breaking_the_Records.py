input()
scores = list(map(int, input().split(' ')))
highest = scores[0]
lowest = scores[0]
break_highest = 0
break_lowest = 0

for i in range(1, len(scores)):
    if scores[i] > highest:
        break_highest += 1
        highest = scores[i]
    if scores[i] < lowest:
        break_lowest += 1
        lowest = scores[i]

print(str(break_highest) + ' ' + str(break_lowest))
