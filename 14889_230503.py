import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global min_diff
    
    if depth == n // 2:
        p1, p2 = 0, 0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    p1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    p2 += graph[i][j]
        
        min_diff = min(min_diff, abs(p1 - p2))
        
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

n = int(input())

visited = [False for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9) # 1e9 : 가능한 최댓값이 10억 미만이라면 무한(INF) 값으로 1e9 이용가능

dfs(0, 0)
print(min_diff)