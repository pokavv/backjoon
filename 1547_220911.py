import sys
num = int(sys.stdin.readline())

cup = [1, 2, 3]
for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    
    xlocation = cup.index(x)
    ylocation = cup.index(y)
    
    cup[xlocation], cup[ylocation] = cup[ylocation], cup[xlocation]

print(cup[0])