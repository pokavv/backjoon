# 이전 코드(230221)
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

####################################################################################

# 수정코드(230612)
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global max_val, min_val
    
    if depth == n:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return
    
    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], operations[0], operations[1], operations[2], operations[3])

print(max_val)
print(min_val)