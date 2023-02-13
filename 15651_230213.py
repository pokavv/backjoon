import sys
input = sys.stdin.readline

def dfs(cnt):
    if cnt - 1 == b:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(1, a + 1):
        nums.append(i)
        dfs(cnt + 1)
        nums.pop()

a, b = map(int, input().split())
nums = []

dfs(1)