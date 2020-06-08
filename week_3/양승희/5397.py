# 정렬/ 스택 - 키로커

for each in range(int(input())):
        input_str = input()
        top = -1
        stack = list()
        for i in input_str:
                if i is '<':
                        if(top is -1):
                                continue
                        top -= 1
                elif i is '>':
                        if(top is -1):
                                continue
                        top += 1
                elif i is '-':
                        if len(stack) is 0:
                                continue
                        print(top)
                        stack.pop(top)
                        top -= 1
                else:
                        top += 1
                        stack.insert(top,i)
                print(stack)
        print("".join(stack))
