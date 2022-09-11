import sys
val_list = []

for i in range(int(sys.stdin.readline())):
    val_list.append(int(sys.stdin.readline()))
    
val = val_list[-1]
if val_list[2] - val_list[1] == val_list[1] - val_list[0]:
    val += val_list[2] - val_list[1]
else:
    val *= val_list[2] // val_list[1]
    
print(val)