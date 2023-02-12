import sys
input = sys.stdin.readline

def dfs(n):
    if len(nums) == b:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(n, a+1):
        if visited[i]:
            continue
        
        visited[i] = True
        nums.append(i)
        dfs(i+1)
        nums.pop()
        
        # print(nums)
        # print(visited)
        visited[i] = False

a, b = map(int, input().split())
nums = []
visited = [False] * (a + 1)

dfs(1)