star_floor = int(input())

for i in range(1, star_floor + 1):
    star = ' ' * (star_floor - i) + '*' * ((2 * i) - 1)
    print(star)