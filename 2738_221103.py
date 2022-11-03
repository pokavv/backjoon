import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    tmp = list(map(int, input().split()))
    
    for j in range(m):
        board[i][j] += tmp[j]

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()