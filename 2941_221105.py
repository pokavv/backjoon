croatia_alp =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
tmp = input()

for i in croatia_alp:
    tmp = tmp.replace(i, 'a')

print(len(tmp))