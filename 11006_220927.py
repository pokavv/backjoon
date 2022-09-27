import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    i = (m * 2) - n
    r = n - m
    
    print(i, r)