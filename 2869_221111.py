import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())
day = (v - b) / (a - b) 

# v / (a - b)일 경우 정상에 올라간뒤에 밤에 내려와서 다음날 다시 올라가야함
# (v - b) / (a - b)

print(math.ceil(day))