number=int(input())
vps=[]
for i in range(number):
    vps.append(input())
    
for i in range(number):
    basic=0
    for j in vps[i]:
        if(j=='('):
           basic=basic+1
        else:
            basic=basic-1
        if(basic<0):
            break
    if(basic==0):
        print("YES")
    else:
        print("NO")