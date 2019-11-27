n = int(input())
ip = sorted([int(input()) for _ in range(n)], reverse=True)
ret = ip[0]
for k in range(2, n+1):
    ret = max(ret, ip[k-1]*k)
print(int(ret))