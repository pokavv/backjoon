import sys
input = sys.stdin.readline

n = int(input())
tri_arr = []

for i in range(n):
    tri_arr.append(list(map(int, input().split())))

# 처음과 끝은 바로 위 숫자를 더하고, 나머지는 대각선 중 최댓값을 더해서 누적시킴

for i in range(1, n):
    for j in range(len(tri_arr[i])):
        if j == 0:
            tri_arr[i][j] += tri_arr[i-1][j]
        elif j == i:
            tri_arr[i][j] += tri_arr[i-1][j-1]
        else:
            tri_arr[i][j] += max(tri_arr[i-1][j], tri_arr[i-1][j-1])

print(max(tri_arr[n-1]))