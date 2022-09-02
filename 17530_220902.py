num = int(input())
max_s = 0
score = []

for i in range(num):
    val = int(input())
    score.append(val)
    if max_s < val:
        max_s = val

if max_s == score[0]:
    print('S')
else:
    print('N')