test_case = int(input())

for i in range(test_case):
    candy, brother_num = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(candy // brother_num, candy % brother_num))