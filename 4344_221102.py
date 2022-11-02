import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    score = list(map(int, input().split()))
    
    n = score[0]
    del(score[0])
    avg = sum(score) / len(score)
    
    for i in score:
        if i > avg:
            cnt += 1
    
    res = cnt / n * 100
    print(f'{res:.3f}%')