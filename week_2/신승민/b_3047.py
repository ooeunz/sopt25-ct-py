import sys

ns = list(map(int, sys.stdin.readline().split()))
# [a, b, c]
ns.sort()
qz = list(map(lambda q: ord(q)-ord('A'), sys.stdin.readline().strip()))
print(' '.join(map(lambda q: str(ns[q]), qz)))
