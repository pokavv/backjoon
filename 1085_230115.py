# x, y를 함께 min 고려해주는 이유:
# x, y좌표를 기준으로 (0, 0)까지의 거리도 고려

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
print(min([x, y, w - x, h - y]))