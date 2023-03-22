import sys
input = sys.stdin.readline

while True:
    lines = sorted(list(map(int, input().split())))
    
    if sum(lines) == 0:
        break
    elif lines[0] + lines[1] <= lines[2]:
        print('Invalid')
    elif lines[0] == lines[1] == lines[2]:
        print('Equilateral')
    elif lines[0] == lines[1] or lines[1] == lines[2] or lines[2] == lines[0]:
        print('Isosceles')
    else:
        print('Scalene')