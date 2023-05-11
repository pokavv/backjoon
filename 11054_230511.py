import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

increase_arr = [1 for _ in range(n)]
decrease_arr = [1 for _ in range(n)]
res = [0 for _ in range(n)]

# increase
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and increase_arr[i] < increase_arr[j] + 1:
            increase_arr[i] = increase_arr[j] + 1

# decrease
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if arr[i] > arr[j] and decrease_arr[i] < decrease_arr[j] + 1:
            decrease_arr[i] = decrease_arr[j] + 1
    
    res[i] = decrease_arr[i] + increase_arr[i] - 1

print(max(res))