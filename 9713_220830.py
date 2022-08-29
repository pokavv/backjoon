test_case = int(input())

for i in range(test_case):
    num = int(input())
    sum = 0
    for j in range(1, num + 1):
        if j % 2 == 1:
            sum += j
    print(sum)