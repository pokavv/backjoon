num = int(input())
arr = []

for i in range(num):
    eat_brain, must_eat_brain = map(int, input().split())
    if eat_brain >= must_eat_brain:
        arr.append('MMM BRAINS')
    else:
        arr.append('NO BRAINS')
for i in arr:
    print(arr[i])