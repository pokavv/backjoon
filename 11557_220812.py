test_case = int(input())

for i in range(test_case):
    school_num = int(input())
    max_L = 0
    maxL_name = ""
    for j in range(school_num):
        name, num = input().split()
        num = int(num)
        if num > max_L:
            max_L = num
            maxL_name = name
    print(maxL_name)