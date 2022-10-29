from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(field, a, b):
    queue = deque()
    queue.append((a, b))
    field[a][b] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= width or ny < 0 or ny >= length:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(int(input())):
    width, length, loc_num = map(int, input().split())
    field = [[0] * length for _ in range(width)]
    cnt = 0
    
    for _ in range(loc_num):
        loc_x, loc_y = map(int, input().split())
        field[loc_x][loc_y] = 1
    
    for a in range(width):
        for b in range(length):
            if field[a][b] == 1:
                bfs(field, a, b)
                cnt += 1
    print(cnt)