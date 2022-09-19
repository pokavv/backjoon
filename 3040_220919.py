dwarf = []
res = False

for i in range(9):
    input_dwarf = int(input())
    dwarf.append(input_dwarf)

for i in range(8):
    if res:
        break
    
    for j in range(i + 1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            dwarf.pop(i)
            dwarf.pop(j - 1)
            
            for b in sorted(dwarf):
                print(b)
            
            res = True
            break