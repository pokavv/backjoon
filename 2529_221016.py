from itertools import permutations

n = int(input())
inequality_sign = input().split()
res = []

for i in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], n + 1):
    isTrue = True
    for j in range(len(inequality_sign)):
        if inequality_sign[j] == '<':
            if i[j] < i[j + 1]:
                continue
            else:
                isTrue = False
                break
        else:
            if i[j] > i[j + 1]:
                continue
            else:
                isTrue = False
                break
    if isTrue:
        res.append(i)

print(''.join(map(str, list(max(res)))))
print(''.join(map(str, list(min(res)))))