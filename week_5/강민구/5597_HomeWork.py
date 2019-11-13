import sys

Attend = list(sys.stdin.readline().strip() for _ in range(28))
Attend = list(map(int,Attend))

for i in range(1,31) :
    if i not in Attend :
        print(i)
