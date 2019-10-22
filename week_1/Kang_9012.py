
##9012번 '괄호'문제
T=int(input())

for i in range(T):
    a=input()
    stack = []

    result = 'YES'
    count = 0

    for j in range(len(a)) :
        if a[j] =='(' :
            stack.append(a[j])
            count+=1
        elif a[j]==')' :
            if not stack :
                result="NO"
                count-=1
                break
            else :
                stack.pop()
                count-=1
        else :
            result="NO"
            count-=1
            break

    if count != 0 :
        result="NO"
    print(result)

