star_floor = int(input())

for i in range(1, star_floor + 1):
    star = "*" * i
    print(star)

for j in range(star_floor - 1, 0, -1):
    reverse_star = "*" * j
    print(reverse_star)