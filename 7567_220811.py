total = 0
bowl = list(input())

for i in range(len(bowl)):
    if i == 0:
        total += 10
    elif bowl[i] == bowl[i-1]:
        total += 5
    else:
        total += 10

print(total)