import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

print(len(set1 - set2) + len(set2 - set1))