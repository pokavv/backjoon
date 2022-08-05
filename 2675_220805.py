Tcase = int(input())

for _ in range(Tcase):
    tnum, tstr = input().split()
    for i in tstr:
        print(i * int(tnum), end='')
    print()