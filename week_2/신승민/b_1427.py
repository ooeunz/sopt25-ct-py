import sys

n = list(sys.stdin.readline().strip())
print(''.join(sorted(n, reverse=True)))