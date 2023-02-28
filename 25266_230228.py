'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

n = int(input())
cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            cnt += 1

print(cnt)
print(3)

################

print(int(input()) ** 3)
print(3)