# 고정비 a, 가변비 b, 가격 c
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)