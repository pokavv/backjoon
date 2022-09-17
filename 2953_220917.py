import sys
man_list = []

for i in range(5):
    score = list(map(int, sys.stdin.readline().split()))
    man_list.append(sum(score))

win_score = max(man_list)
man_num = man_list.index(max(man_list))
print(man_num + 1, win_score)