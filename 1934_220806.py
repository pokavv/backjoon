test_case = int(input())

for i in range(test_case):
    n = 0
    num1, num2 = map(int, input().split())
    a, b = num1, num2

    # if (둘 중 작은 수)의 최대공약수 == (큰 수 % 작은 수)의 최대공약수
    ## 최대공약수 식: a, b = b, a % b
    ## 최소공배수 식: (a * b) // 최대공약수 
    while b != 0:
        a = a % b
        a, b = b, a
    print(num1 * num2 // a)