for _ in range(int(input())):
    floor = int(input())
    num = int(input())
    people = [i for i in range(1, num + 1)]
    
    for _ in range(floor):
        new = []
        for j in range(num):
            new.append(sum(people[:j+1]))
        people = new.copy()
    print(people[-1])