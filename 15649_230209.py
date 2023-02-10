def dfs():
    if len(nums) == b:
        print(' '.join(map(str, nums)))
        return
    for i in range(1, a+1):
        if visited[i]:
            continue
        
        visited[i] = True
        nums.append(i)
        dfs()
        nums.pop()
        
        # print(nums)
        # print(visited)
        visited[i] = False

a, b = map(int, input().split())
nums = []
visited = [False] * (a + 1)

dfs()

'''
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
'''