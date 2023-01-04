import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

print(board)