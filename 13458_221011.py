import sys
input = sys.stdin.readline

exam_room = int(input())
tester = list(map(int, input().split()))
a, b = map(int, input().split())
cnt = exam_room

for i in tester:
    i -= a
    if i > 0:
        if i % b:
            cnt += (i // b) + 1
        else:
            cnt += (i // b)

print(cnt)