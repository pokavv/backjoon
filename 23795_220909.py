import sys
money = 0

while True:
    i = int(sys.stdin.readline())
    if i < 0:
        break
    money += i

print(money)