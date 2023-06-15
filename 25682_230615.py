import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

def chess(color):
    dp = [[0] * (m+1) for i in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                val = board[i][j] != color
            else:
                val = board[i][j] == color
            
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + val
    
    cnt = 1e9
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            cnt = min(cnt, dp[i+k-1][j+k-1] - dp[i+k-1][j-1] - dp[i-1][j+k-1] + dp[i-1][j-1])
    
    return cnt

print(min(chess('W'), chess('B')))