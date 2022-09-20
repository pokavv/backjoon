import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p1 = p2 = 0
    for i in range(int(input())):
        p1_hand, p2_hand = input().split()
        if p1_hand == p2_hand:
            continue
        elif (p1_hand == 'R' and p2_hand == 'S') or (p1_hand == 'P' and p2_hand == 'R') or (p1_hand == 'S' and p2_hand == 'P'):
            p1 += 1
        else:
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")