arr = []

for i in range(int(input())):
    st = input()
    arr.append(st)
    print(f'{arr.index(st) + 1}. {st}')