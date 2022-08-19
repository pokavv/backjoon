star_floor = int(input())

for i in range(1, star_floor + 1):
    star = (" " * (star_floor - i)) + ("*" * i)
    print(star)

for j in range(1, star_floor):
    reverse_star = (" " * j) + ("*" * (star_floor - j))
    print(reverse_star)