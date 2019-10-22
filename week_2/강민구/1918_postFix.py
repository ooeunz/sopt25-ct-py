def weight(word) : # 값 하나하나 가중치를 주는 함수
    if word == '*' or word =='/' :
        return 5
    elif word == '+' or word == '-' :
        return 3
    elif word =='(' :
        return 1
    else :
        return -1

def postFix(a): # 후위 표기식을 실행하는 함수
    post_List = []
    stack = []

    for ch in a :
        ch_Weight = weight(ch)

        if ch == '(' :
            stack.append(ch)
            continue
        elif ch == ')' :
            while stack and stack[-1] != "(" : # '(' 가 나올 때 까지 스택에서 pop
                post_List.append(stack.pop())
            stack.pop() # 남은 '('를 pop()
            continue
        elif ch == '*' or ch == '/' or ch == '+' or ch == '-' : # 사칙연산 계산
            while stack and weight(stack[-1]) >= ch_Weight : #stack의 top에 있는 값의 가중치가 클 경우 계속해서 pop
                post_List.append(stack.pop())
            stack.append(ch)
            continue
        else :
            post_List.append(ch)
            continue

    while stack :
        post_List.append(stack.pop())

    return post_List



if __name__ == "__main__" :
    a = list(input())
    print(''.join(postFix(a)))
