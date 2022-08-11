test_case = int(input())
for i in range(test_case):
    OX = input()
    OX_list = list(OX)
    sum_score = 0
    score = 1
    for i in OX_list:
        if i == 'O':
            sum_score += score
            score += 1
        else:
            score = 1
    print(sum_score)