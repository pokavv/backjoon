score_sum = 0
score_list = []
tmp = []

for i in range(8):
    score = int(input())
    if score >= 0 and score <= 150:
        score_list.append(score)

for i in range(5):
    score_sum += max(score_list)
    tmp.append(score_list.index(max(score_list)) + 1)
    score_list[score_list.index(max(score_list))] = -1

tmp.sort()
print(score_sum)
print(*tmp)