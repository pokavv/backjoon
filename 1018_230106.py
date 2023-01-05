import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

res = []

for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        black = 0
        
        for row in range(i, i + 8):
            for column in range(j, j + 8):
                if (row + column) % 2 == 0:
                    if board[row][column] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[row][column] != 'B':
                        white += 1
                    else:
                        black += 1
        res.append(white)
        res.append(black)

print(min(res))