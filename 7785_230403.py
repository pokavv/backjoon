import sys
input = sys.stdin.readline
employee = {}

for _ in range(int(input())):
    name, state = input().split()
    employee[name] = state
    
    if state == 'leave':
        del employee[name]

employee = dict(sorted(employee.items(), reverse=True))

for k in employee.keys():
    print(k)