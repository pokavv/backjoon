star_floor = int(input())

for i in range(1, star_floor + 1):
    star = "*" * i + " " * ((-2) * i + star_floor * 2) + "*" * i
    print(star)

for j in range(star_floor - 1, 0, -1):
    reverse_star = "*" * j + " " * ((-2) * j + star_floor * 2) + "*" * j
    print(reverse_star)