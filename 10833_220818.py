apple_sum = 0

for i in range(int(input())):
    student_sum, apple = map(int, input().split())
    apple_sum += apple % student_sum
print(apple_sum)