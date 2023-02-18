import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
row = [0] * n
visited1 = [False] * n
visited2 = [False] * (2*n-1)
visited3 = [False] * (2*n-1)

def n_queens(x):
    global cnt
    if x == n:
        cnt += 1
        return

    else:
        for i in range(n):
            # [x, i] 퀸 배치
            if not visited1[i] and not visited2[x+i] and not visited3[x-i+n-1]:
                row[x] = i
                visited1[i] = True
                visited2[x+i] = True
                visited3[x-i+n-1] = True
                n_queens(x+1)
                visited1[i] = False
                visited2[x+i] = False
                visited3[x-i+n-1] = False

n_queens(0)
print(cnt)