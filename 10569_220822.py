test_case = int(input())

for i in range(test_case):
    vertex, edge = map(int, input().split())
    print(2 - (vertex - edge))