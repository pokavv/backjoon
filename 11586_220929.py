mirror = []

for _ in range(int(input())):
    val = input()
    mirror.append(val)

mind_state = int(input())

if mind_state == 1:
    for i in range(len(mirror)):
        print(mirror[i])
elif mind_state == 2:
    for i in range(len(mirror)):
        print(mirror[i][::-1])
else:
    for i in range(len(mirror)-1, -1, -1):
        print(mirror[i])