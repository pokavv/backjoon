import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split())
    cnt = 0
    
    for x in range(1, a - 1):
        for y in range(x + 1, a):
            if (x ** 2 + y ** 2 + b) % (x * y) == 0:
                cnt += 1
    print(cnt)