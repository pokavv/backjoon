dice_round = int(input())
score1 = 100
score2 = 100

for i in range(dice_round):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        score2 -= num1
    elif num1 < num2:
        score1 -= num2

print(score1, score2, sep = "\n")