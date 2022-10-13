import sys
input = sys.stdin.readline

def bt(idx):
    for i in range(1, (idx // 2) + 1):
        if s[-1:] == s[-2 * i:-1]:
            return -1