import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(i, arr):
    global max_val, min_val, add, sub, mul, div
    
    if i == n:
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, arr + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, arr * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(arr / nums[i]))
            div += 1

dfs(1, nums[0])

print(max_val)
print(min_val)