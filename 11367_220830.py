for _ in range(int(input())):
    name, num = input().split()
    num = int(num)
    if num >= 97: grade = "A+"
    elif num >= 90: grade = "A"
    elif num >= 87: grade = "B+"
    elif num >= 80: grade = "B"
    elif num >= 77: grade = "C+"
    elif num >= 70: grade = "C"
    elif num >= 67: grade = "D+"
    elif num >= 60: grade = "D"
    else: grade = "F"
    print(name, grade)