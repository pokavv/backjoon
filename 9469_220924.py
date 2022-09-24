import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, d, a, b, f = map(float, input().split())
    mile = (d / (a + b)) * f
    print(f'{n} %.6f' % mile)