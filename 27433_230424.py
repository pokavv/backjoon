n = int(input())

def fact(n):
    if n > 0:
        return n * fact(n - 1)
    else:
        return 1

print(fact(n))

###################################

import math

n = int(input())

def fact_2(n):
    return math.factorial(n)

print(fact_2(n))

####################################

n = int(input())

if n == 0:
    print(1)
else:
    res = 1
    for i in range(2, n + 1):
        res *= i
    print(res)