import sys
input = sys.stdin.readline

passenger = 0
max_passenger = 0

for i in range(10):
    get_off, get_on = map(int, input().split())
    if max_passenger < passenger - get_off + get_on:
        max_passenger = passenger - get_off + get_on
    passenger = passenger - get_off + get_on

print(max_passenger)