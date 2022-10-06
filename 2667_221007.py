from collections import deque

num = int(input())
board = [list(map(int, input())) for _ in range(num)]

def bfs(board, x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    qu = deque()
    qu.append((x, y))
    board[x][y] = 0 # isVisited
    cnt = 1
    
    while qu:
        x, y = qu.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= num or ny < 0 or ny >= num:
                continue
            
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                qu.append((nx, ny))
                cnt += 1
    return cnt

search = [bfs(board, i, j) for i in range(num) for j in range(num) if board[i][j] == 1]
search.sort()
print(len(search))

for i in range(len(search)):
    print(search[i])