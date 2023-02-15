import sys
input = sys.stdin.readline

def dfs(cnt):
    if len(nums) == b:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(cnt, a+1):
        nums.append(i)
        dfs(i)
        nums.pop()

a, b = map(int, input().split())
nums = []

dfs(1)