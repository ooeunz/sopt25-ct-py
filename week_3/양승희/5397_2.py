cnt = int(input())

for each in range(cnt):
        input_str = input()
        top = -1
        stack = list()
        for i in input_str:
                if i is '<':
                        print(top)
                        if(top < 1):
                                continue
                        top -= 1
                elif i is '>':
                        if(top is -1):
                                continue
                        elif(top == len(stack)):
                                continue
                        top += 1
                elif i is '-':
                        print(top)
                        if(top is -1):
                                continue
                        stack.pop(top)
                        top -= 1
                else:
                        print(top)
                        top += 1
                        stack.insert(top,i)
        print("".join(stack))