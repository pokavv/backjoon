import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
res = set()

for i in range(n):
    arr.append(int(input()))

def dfs(a, b, num):
    a.add(num)
    b.add(arr[num])
    if arr[num] in a:
        if a == b:
            res.update(a)
            return True
        return False
    return dfs(a, b, arr[num])

for i in range(1, n + 1):
    if i not in res:
        dfs(set(), set(), i)

print(len(res))
print(*sorted(list(res)), sep='\n')