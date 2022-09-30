import sys
input = sys.stdin.readline

lleg, rleg, all = map(int, input().split())
min_val, max_val = min(lleg, rleg), max(lleg, rleg)
n = min(all, max_val - min_val)

min_val += n
all -= n
res = (min_val * 2) + (all // 2 * 2 if all else 0)
print(res)