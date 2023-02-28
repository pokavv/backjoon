'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

n = int(input())
cnt = 0

for i in range(1, n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n + 1):
            cnt += 1

print(cnt)
print(3)

###########

print(((n - 2) * (n - 1) * (2 * n - 3) + 3 * (n - 1) * (n - 2)) // 12)
print(3)