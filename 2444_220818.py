star_floor = int(input())

for i in range(1, star_floor + 1):
    star = " " * (star_floor - i) + "*" * ((2 * i) - 1)
    print(star)

for j in range(star_floor - 1, 0, -1):
    reverse_star = " " * (star_floor - j) + "*" * ((2 * j) - 1)
    print(reverse_star)