star_floor = int(input())

for i in range(star_floor, 0, -1):
    star = " " * (star_floor - i) + "*" * ((2 * i) - 1)
    print(star)