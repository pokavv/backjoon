import sys
import itertools
input = sys.stdin.readline

a, b = map(int, input().split())
nums = [i for i in range(1, a + 1)]

arr = itertools.permutations(nums, b)

for i in arr:
    for j in i:
        print(j, end=' ')
    print()