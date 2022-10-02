import sys
input = sys.stdin.readline

won, xN = map(int, input().split())
if xN == 1:
    print(-1)
else:
    res = (won * xN) // (xN - 1)
    if (won * xN) % (xN - 1) > 0:
        res += 1
    print(res)