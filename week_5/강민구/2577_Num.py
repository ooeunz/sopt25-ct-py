A = int(input())
B = int(input())
C = int(input())

result = list(map(int,str(A*B*C)))

for i in range(10) :
    print(result.count(str(i)))






