test_case = int(input())

for i in range(test_case):
    pb = int(input())
    for j in range(pb):
        num = list(map(int, input().split()))
        print(num[0] + num[1], num[0] * num[1])