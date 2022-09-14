st = ''

for i in input():
    if i.islower():
        st += i.upper()
    else:
        st += i.lower()
print(st)