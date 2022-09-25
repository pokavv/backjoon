work_num, time = map(int, input().split())
li = list(map(int, input().split()))

for i in range(work_num):
    if sum(li[:i+1]) > time:
        print(i)
        break
    elif i == work_num - 1:
        print(work_num)