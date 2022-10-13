from collections import deque
import queue

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, graph, color):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = '0'
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                graph[nx][ny] = '0'
                queue.append((nx, ny))

n = int(input())
graph = []
R_graph = [['0'] * n for i in range(n)]
cnt = 0
Rcnt = 0

for i in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            R_graph[i][j] = 'R'
        else:
            R_graph[i][j] = graph[i][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] in 'RGB':
            bfs(i, j, graph, graph[i][j])
            cnt += 1
        
        if R_graph[i][j] in 'RB':
            bfs(i, j, R_graph, R_graph[i][j])
            Rcnt += 1

print(cnt, Rcnt)