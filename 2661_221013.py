def func(index) :
    global data

    for i in range(1, (index // 2) + 1) :
        if data[-i:] == data[-2*i:-i] :
            return -1

    if index == n :
        for i in range(n) :
            print(data[i], end='')
        return 0

    for i in range(1, 4) :
        data.append(i)
        if func(index + 1)  == 0:
            return 0
        data.pop()

n = int(input())
data = []
func(0)