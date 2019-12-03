def plus(a):
    if(a==1):
        return 1
    elif(a==2):
        return 2
    elif(a==3):
        return 4
    else:
        return plus(a-3)+plus(a-2)+plus(a-1)
a = int(input())
for _ in range(a):
    print(plus(int(input())))