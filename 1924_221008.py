import sys
input = sys.stdin.readline
m, d = map(int, input().split())

day = 0
end_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(m - 1):
    day = day + end_month[i]
day = (day + d) % 7

print(date[day])

'''
# calendar module
import calendar

m, d = map(int, input().split())
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day = calendar.weekday(2007, m, y)
print(date[day])
'''