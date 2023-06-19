import sys
input = sys.stdin.readline

form = input().split("-")
res = sum(map(int, form[0].split("+")))

for i in range(1, len(form)):
    tmp = sum(map(int, form[i].split("+")))
    res -= tmp

print(res)