def isVPS(size):
    if size == 0 :
        print("YES")
        return

    print("NO")

if __name__ == "__main__":
    input_cnt = input()

    for i in range(0,int(input_cnt),1):
        stack = list()
        input_str = input()
        stack_size = len(stack)

        for each in input_str:
            if each is '(':
                stack.append(each)
            elif each is ')' and len(stack) == 0:
                stack_size = -1
                break
            elif each is ')':
                stack.pop()
            
            stack_size = len(stack)

        isVPS(stack_size)