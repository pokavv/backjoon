st = input()
key = input()
without_num = ''

for i in st:
    if 48 <= ord(i) <= 57: # 숫자
        pass
    else:
        without_num += i # 숫자가 아닌 문자

if key in without_num:
    print(1)
else:
    print(0)