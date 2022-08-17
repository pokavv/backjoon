semester = int(input())

arr = []

for i in range(semester):
    subject = int(input())
    total_credit = 0
    total_grade = 0

    for _ in range(subject):
        credit, grade = map(float, input().split())
        total_credit += credit
        total_grade += credit * grade

    GPA = total_grade / total_credit
    print(int(total_credit), '%.1f' % GPA)