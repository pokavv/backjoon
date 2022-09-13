def money():
    ls = sorted(list(map(int, input().split())))
    if len(set(ls)) == 1:
        return ls[0] * 5000 + 50000
    
    if len(set(ls)) == 2:
        if ls[1] == ls[2]:
            return ls[1] * 1000 + 10000
        else:
            return (ls[1] + ls[2]) * 500 + 2000
    
    for i in range(3):
        if ls[i] == ls[i+1]:
            return ls[i] * 100 + 1000
    return ls[-1] * 100

N = int(input())
print(max(money() for i in range(N)))