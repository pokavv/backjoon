import sys
input = sys.stdin.readline
member = []

for _ in range(int(input())):
    age, name = map(str, input().split())
    age = int(age)
    member.append((age, name))

member.sort(key=lambda list: list[0])

for i in member:
    print(i[0], i[1])