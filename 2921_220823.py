domino_vol = int(input())
domino_set_dot = 0

for i in range(0, domino_vol + 1):
    for j in range(i, domino_vol + 1):
        domino_set_dot += i + j
print(domino_set_dot)