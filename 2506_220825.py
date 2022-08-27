problem_num = int(input())
score_stack = 0
sum_score = 0

problem = list(map(int, input().split()))

for i in range(problem_num):
    if problem[i] == 1:
        score_stack += 1
        sum_score += score_stack
    else:
        score_stack = 0

print(sum_score)