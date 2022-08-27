subject_num = int(input())
subject_score_list = list(map(int, input().split()))
max_score = max(subject_score_list)
modified_score = 0

for i in subject_score_list:
    modified_score += (i / max_score) * 100
print(modified_score / subject_num)