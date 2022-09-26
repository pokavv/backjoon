num = int(input())
num_arr = list(map(int, input().split()))
arr = []
arr.append(num_arr[0])

for i in range(1, num):
    arr.append((num_arr[i] * (i + 1)) - sum(arr))

for j in arr:
    print(j, end=' ')