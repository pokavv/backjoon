import sys
input = sys.stdin.readline

num = int(input())

connect_total = 0
for i in range(num):
    connect_total += int(input())

print(connect_total - (num - 1))