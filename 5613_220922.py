res = int(input())

while 1:
    val = input()
    if val == '=':
        break
    n = int(input())
    if val == '+': res += n
    elif val == '-': res -= n
    elif val == '*': res *= n
    elif val == '/': res //= n
    
print(res)