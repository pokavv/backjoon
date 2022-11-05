import sys
input = sys.stdin.readline
alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input_alp = list(input())
time = 0

for i in input_alp:
    for j in alp:
        if i in j:
            time += alp.index(j) + 3

print(time)