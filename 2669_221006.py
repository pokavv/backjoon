import sys
input = sys.stdin.readline
board = [[0] * 100 for _ in range(101)]
cnt = 0

for i in range(4):
    i, j, x, y = map(int, input().split())
    
    for a in range(i, x): 
        for b in range(j, y):
            if board[a][b] == 0:
                board[a][b] += 1
                cnt += 1

print(cnt)