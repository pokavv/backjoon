import sys
input = sys.stdin.readline

one_hand, no_look, pon = map(int, input().split())
club = int(input())
res = 0

for i in range(club):
    score = 0
    for j in range(3):
        use_one_hand, use_no_look, use_pon = map(int, input().split())
        score += (one_hand * use_one_hand) + (no_look * use_no_look) + (pon * use_pon)
    
    res = max(res, score)

print(res)