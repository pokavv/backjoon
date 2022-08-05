A = int(input())
cal = str(input())
B = int(input())

def Calculate():
    if cal == '*':
        print(A * B)
    elif cal == '+':
        print(A + B)
    else:
        exit()

Calculate()
