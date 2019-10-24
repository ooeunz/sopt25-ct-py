stick=input().replace('()','/')
raiser=0
result=0
for i in stick:
    if(i=='/'):
        result=result+raiser
    elif(i=='('):
        raiser=raiser+1
    else:
        raiser=raiser-1
        result=result+1
print(result)