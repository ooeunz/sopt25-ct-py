# 검사할 문자열 개수 받기
num = int(input())
vps = []
stack_list = []
ans = []

class Stack(list):
    push = list.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False
    
    def peek(self):
        return self[-1]

# 리스트 vps에 받을 문자열 개수만큼 리스트 생성
for i in range(num):
    vps = vps + [i]
    
for index in range(len(vps)):
    # 입력받은 vps 문자열 리스트화
    par = list(input())
    stack = Stack(stack_list)

    for s in range(len(par)):
        if par[s] == '(':
            stack.push('(')
            
        elif par[s] == ')':
            if stack.is_empty() == True:
                stack.push(-1)
                break
            else:
                stack.pop()
    if stack == []:
       ans.append('YES')
    else:
        ans.append('NO')
    
for YN in range(len(ans)):
    print(ans[YN])
    

