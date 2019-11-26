import sys
N = int(input())
rope = [sys.stdin.readline().strip() for _ in range(N)]
rope = sorted(list(map(int,rope)))
max_weight = 0
for i in range(N) :
    max_weight = max(max_weight,rope[i] * (N-i))
print(max_weight)