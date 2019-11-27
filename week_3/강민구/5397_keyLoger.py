def findPassword(a) :
    password_List = [] # 패스워드를 넣는 리스트
    sub_List =[] # 문자를 잠시 보관하는 스택

    for word in a :
        if word == "<" : # sub_List에 맨 끝 단어 저장
            if not password_List :
                continue
            else :
                sub_List.append(password_List.pop())

        elif word == ">" : # sub_list에서 pop 하여 다시 패스워드 리스트에 저장
            if not sub_List :
                continue
            else :
                password_List.append(sub_List.pop())

        elif word =="-" : # 단어 삭제
            if not password_List :
                continue
            else :
                password_List.pop()

        else :
            password_List.append(word)

    #남아있는 sub_list 원소를 전부 pop
    for _ in range(len(sub_List)) :
        password_List.append(sub_List.pop())

    return password_List


if __name__ == "__main__" :
    T = int(input())

    for _ in range(T) :
        a = list(input())
        print(''.join(findPassword(a)))
