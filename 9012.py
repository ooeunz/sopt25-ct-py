class stack_class:
    def __init__(self):
        self.__stack_list = list()
    
    def push(self, value):       
        self.__stack_list.append(value)

    def pop(self):       
        self.__stack_list.pop()

    def size(self):
        return len(self.__stack_list)

def isVPS(size):
    if size == 0 :
        print("YES")
        return

    print("NO")

if __name__ == "__main__":
    input_cnt = input()

    for i in range(0,int(input_cnt),1):
        stack = stack_class()
        input_str = input()
        stack_size = stack.size()   

        for each in input_str:
            if each is '(':
                stack.push(each)
            elif each is ')' and stack.size() == 0:
                stack_size = -1
                break
            elif each is ')':
                stack.pop()
            
            stack_size = stack.size()

        isVPS(stack_size)