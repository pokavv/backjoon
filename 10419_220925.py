import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    mt = 0
    
    while (mt + 1) + (mt + 1) ** 2 <= n:
        mt += 1

    print(mt)