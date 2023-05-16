import sys
input = sys.stdin.readline

# 문제 지문 속 함수 w()
def original_w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    
    return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

# dp를 이용한 함수 w()
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif arr[a][b][c]:
        return arr[a][b][c]
    elif a < b < c:
        arr[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return arr[a][b][c]
    
    arr[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return arr[a][b][c]

arr = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')