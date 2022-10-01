import sys
input = sys.stdin.readline

man_y, man_m, man_d = map(int, input().split())
y, m, d = map(int, input().split())
age = 0

if man_m < m:
    age = y - man_y
elif man_m == m:
    if man_d <= d:
        age = y - man_y
    else:
        age = y - man_y - 1
else:
    age = y - man_y - 1

cnt_age = y - man_y + 1
cnt_year = y - man_y

print(age)
print(cnt_age)
print(cnt_year)