import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = sorted(map(int, input().split()))
    score = score[1:4]
    
    if score[2] - score[0] >= 4:
        print('KIN')
    else:
        print(sum(score))