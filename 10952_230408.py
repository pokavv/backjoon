arr = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        arr.append(a + b)

for i in range(len(arr)):
    print(arr[i])