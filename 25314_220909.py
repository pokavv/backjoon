import sys
num = sys.stdin.readline()

val = 'long ' * (int(num) // 4) + 'int'
print(val)