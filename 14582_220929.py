woolim = list(map(int, input().split()))
startlink = list(map(int, input().split()))

woolim_sum_score = 0
startlink_sum_score = 0
reversal = False

for i in range(9):
    woolim_sum_score += woolim[i]
    if woolim_sum_score > startlink_sum_score:
        reversal = True
    startlink_sum_score += startlink[i]

if woolim_sum_score < startlink_sum_score and reversal == True:
    print('Yes')
else:
    print('No')