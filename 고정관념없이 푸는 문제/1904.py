n = int(input())
a=1
b=2
c =0
for i in range(n-1):
    c = a
    a = b
    b = (c+b)%15746
print(a)