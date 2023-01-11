import sys
input = sys.stdin.readline

n = int(input())
card_n = map(int, input().split())
m = int(input())
card_m = map(int, input().split())

card_dict = {}
for i in card_n:
    if i in card_dict:
        card_dict[i] += 1
    else:
        card_dict[i] = 1

res = ''
print(' '.join(str(card_dict[i]) if i in card_dict else '0' for i in card_m))