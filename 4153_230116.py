import sys
input = sys.stdin.readline

while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break
    else:
        length = sorted([x, y, z])
        if length[0] ** 2 + length[1] ** 2 == length[2] ** 2:
            print('right')
        else:
            print('wrong')