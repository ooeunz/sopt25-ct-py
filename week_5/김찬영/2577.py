num1 = int(input())
num2 = int(input())
num3 = int(input())
a = list(str(num1*num2*num3))
a = list(map(int,a))
result = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    for j in range(len(a)):
        if(a[j]==i):
            result[i]=result[i]+1
for i in result:
    print(i)