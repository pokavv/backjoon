import sys
input = sys.stdin.readline

team_num, cmc, pmc = map(int, input().split())
res = []
cnt = 0

for i in range(team_num):
    team = list(map(int, input().split()))
    canPass = True
    
    for i in team:
        if i < pmc:
            canPass = False
            break
    
    if canPass:
        if sum(team) >= cmc:
            res.extend(team)
            cnt += 1

print(cnt)
print(*res)