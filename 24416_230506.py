# python3는 시간초과, pypy3는 통과

def fib_recursion(n):
    global cnt_recursion
    cnt_recursion += 1
    
    if n == 1 or n == 2:
        cnt_recursion -= 1
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)

def fib_dp(n):
    global cnt_dp
    board = [0] * (n + 1)
    board[1], board[2] = 1, 1
    
    for i in range(3, n + 1):
        cnt_dp += 1
        board[i] = board[i - 1] + board[i - 2]
    
    return board[n]

n = int(input())
cnt_recursion, cnt_dp = 0, 0

fib_recursion(n)
fib_dp(n)
print(cnt_recursion + 1, cnt_dp)

##################################################################

def fib(n):
    global cnt
    board = [1] * (n + 1)
    
    for i in range(3, n + 1):
        cnt += 1
        board[i] = board[i - 1] + board[i - 2]
    return board[n]

n = int(input())
cnt = 0

print(fib(n), cnt)