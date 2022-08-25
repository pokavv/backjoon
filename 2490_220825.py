arr = []

for i in range(3):
    num_list = list(map(int, input().split()))
    if num_list.count(0) == 0:
        arr.append('E')
    elif num_list.count(0) == 1:
        arr.append('A')
    elif num_list.count(0) == 2:
        arr.append('B')
    elif num_list.count(0) == 3:
        arr.append('C')
    elif num_list.count(0) == 4:
        arr.append('D')

for i in arr:
    print(arr[i])