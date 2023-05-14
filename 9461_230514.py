padovan_sequence = [0 for _ in range(101)]
test_case = int(input())

padovan_sequence[1] = 1
padovan_sequence[2] = 1
padovan_sequence[3] = 1

for i in range(4, 101):
    padovan_sequence[i] = padovan_sequence[i - 3] + padovan_sequence[i - 2]

for i in range(test_case):
    n = int(input())
    print(padovan_sequence[n])