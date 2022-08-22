star_floor = int(input())

for i in range(1, star_floor + 1):
    star = (" " * (i - 1)) + ("*" * (2 * (star_floor - i) + 1))
    print(star)

for j in range(1, star_floor):
    reverse_star = (" " * (star_floor - j - 1)) + ("*" * ((2 * j) + 1))
    print(reverse_star)