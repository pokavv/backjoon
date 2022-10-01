import sys
input = sys.stdin.readline

fruits_num, length = map(int, input().split())
fruit_list = list(map(int, input().split()))
fruit_list.sort()

for i in range(len(fruit_list)):
    if length >= fruit_list[i]:
        length += 1

print(length)