test_case = int(input())
arr = []

for i in range(test_case):
    a, b = map(int, input().split())
    arr.append(a + b)

for i in arr:
    print(i)