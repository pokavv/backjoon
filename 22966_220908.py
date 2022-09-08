num = int(input())

title = [0]*num
diff = [0]*num

for i in range(num):
    Str=input()
    title[i]=Str[:len(Str)-2]
    diff[i]=int(Str[-1])

Dict=dict(zip(diff,map))

print(Dict[min(Dict.keys())])