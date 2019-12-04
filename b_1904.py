n = int(input())

a = []
a.append(1)
a.append(2)
for i in range(2,n+1):
    a.append((a[i-1] + a[i-2])%15746)

print(a[n-1])