import sys

thinks = list(map(int, sys.stdin.readline().split()))
thinks.sort()
print(thinks[0] * thinks[2])
