# 1. pypy3 통과, python3 시간초과

import sys
input = sys.stdin.readline

def sudoku(tmp_y, tmp_x, n):
    y = (tmp_y // 3) * 3
    x = (tmp_x // 3) * 3
    
    for i in range(9):
        if board[tmp_y][i] == n:
            return False
        if board[i][tmp_x] == n:
            return False
        
        if board[y + i // 3][x + i % 3] == n:
            return False
    return True

def dfs(idx):
    if idx == len(blank):
        for y in range(9):
            print(*board[y])
        exit(0)
    
    y, x = blank[idx]
    for i in range(1, 10):
        if sudoku(y, x, i):
            board[y][x] = i
            dfs(idx + 1)
            board[y][x] = 0

################################

board = [list(map(int, input().split())) for _ in range(9)]
blank = []

for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            blank.append((y, x))

dfs(0)