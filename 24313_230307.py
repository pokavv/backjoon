import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

def asymptotic_notation(a1, a0, c, n0):
    res = set()
    
    for i in range(n0, 101):
        Fn = (a1 * i) + a0
        Gn = i
        
        if Fn <= c * Gn:
            res.add(1)
        else:
            res.add(0)

    if 0 in res:
        print(0)
    else:
        print(1)

asymptotic_notation(a1, a0, c, n0)