import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= length or y <= -1 or y >= width:
        return
    elif field[x][y] == 0:
        return
    field[x][y] = 0
    [x - 1, y]
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)

for i in range(int(input())):
    width, length, loc_num = map(int, input().split())
    field = [[0] * width for _ in range(length)]
    cnt = 0
    
    for _ in range(loc_num):
        loc_x, loc_y = map(int, input().split())
        field[loc_y][loc_x] = 1
    
    for k in range(length):
        for l in range(width):
            if field[k][l] == 1:
                dfs(k, l)
                cnt += 1
    
    print(cnt)