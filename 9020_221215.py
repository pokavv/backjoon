# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 
# 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.

prime_num = [0 for i in range(10001)]
prime_num[1] = 1

for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        prime_num[j] = 1

for i in range(int(input())):
    n1 = int(input())
    n2 = n1 // 2
    
    for j in range(n2, 1, -1):
        if prime_num[n1 - j] == 0 and prime_num[j] == 0:
            print(j, n1 - j)
            break