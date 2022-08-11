while 1:
    arr = []
    n = int(input())
    if n == -1:
        break
    for i in range(2, n//2+1):
        if n % i == 0:
            arr.append(i)
    if sum(arr) + 1 == n:
        print('{0} = 1 '.format(n), end = '')
        for j in arr:
            print('+ {0} '.format(j) ,end = '')
    else:
        print('{0} is NOT perfect. '.format(n))