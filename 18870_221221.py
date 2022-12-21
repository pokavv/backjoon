import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(list(set(numbers)))
sorted_numbers = {sorted_numbers[i]:i for i in range(len(sorted_numbers))}

for i in numbers:
    print(sorted_numbers[i], end=' ')