board = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])