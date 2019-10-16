a = int(input())
vps = []
result = []

for i in range(a):
    ps = input()
    array = list(ps)
    if ps.count('(') == ps.count(')'): #( )개수 같아야 하는 조건
        for j in range(len(array)):
            if array[j]=='(':          # ( 계속 추가
                vps.append(array[j])
            elif vps and array[j]==')': # )일때는 맨끝거 삭제
                del vps[-1]
            else:
                result.append("NO")
                break
        if not vps: #When vps is NULL
            if len(result)==i:
               result.append("YES")

    else:                           #( )개수 같지 않으면 애초부터 NO!
        result.append("NO")

for i in range(len(result)):
    print(result[i])
