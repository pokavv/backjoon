students = int(input())
students_list = []

for i in range(students):
    name, day, month, year = input().split()
    students_list.append([name, int(day), int(month), int(year)])
students_list.sort(key=lambda x: (x[3], x[2], x[1]))
print(students_list[-1][0])
print(students_list[0][0])