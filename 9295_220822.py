test_case = int(input())

for i in range(1, test_case + 1):
    dice1, dice2 = map(int, input().split())
    print("Case ", i, ": ", dice1 + dice2, sep='')