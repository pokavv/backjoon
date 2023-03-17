import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
trees = []
gaps = []

for i in range(n):
    trees.append(int(input()))
    if i > 0:
        gaps.append(trees[i] - trees[i - 1])

# 최대공약수 구하는 gcd 함수
max_gap = gcd(gaps[0], gaps[1])
for i in range(1, n - 1):
    max_gap = gcd(max_gap, gaps[i])

# 놓을 수 있는 전체 나무의 수 - 주어진 나무 수 n = 심어야 하는 나무 수
print(((trees[-1] - trees[0]) // max_gap + 1) - n)