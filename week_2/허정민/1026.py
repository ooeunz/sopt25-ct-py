N = int(input())

A = list(map(int, input().split()))# 각 리스트마다 하나씩 들어감
B = list(map(int, input().split()))

A.sort()
B.sort()

S = 0

for i in range(N):
    S += A[i]*B[N-i -1]

print(S)
