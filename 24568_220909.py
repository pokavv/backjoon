import sys
regular = int(sys.stdin.readline())
small = int(sys.stdin.readline())

whole = (regular * 8) + (small * 3)
output = whole - 28

if output < 0:
    output = 0

print(output)