import sys
input = sys.stdin.readline

t = int(input())
n_arr = [0] * t
max_n = 0

for i in range(t):
    n = int(input())
    n_arr[i] = n
    
    if max_n < n:
        max_n = n

prime_arr = [True] * (max_n + 1)
prime_arr[1] = False

for i in range(2, int(max_n ** 0.5) + 1):
    if prime_arr[i]:
        for j in range(i + i, max_n + 1, i):
            prime_arr[j] = False

for i in n_arr:
    ck = 0
    for j in range(2, i // 2 + 1):
        if prime_arr[j] and prime_arr[i - j]:
            ck += 1
    
    print(ck)