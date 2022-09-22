import sys

num = int(sys.stdin.readline())

while True:
    val = int(sys.stdin.readline())
    if val != 0:
        if val % num == 0:
            print(f'{val} is a multiple of {num}.')
        else:
            print(f'{val} is NOT a multiple of {num}.')
    else:
        break