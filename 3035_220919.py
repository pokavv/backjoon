r, c, zr, zc = map(int, input().split())
val = 0

for i in range(r):
    news = input()
    for j in range(zr):
        for b in range(c):
            res = news[b] * zc
            print(res, end='')
        print()