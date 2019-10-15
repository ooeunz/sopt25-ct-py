class stack_class:
    def __init__(self):
        self.__stack_list = list()
    
    def push(self, value):       
        self.__stack_list.append(value)

    def pop(self):
        self.__stack_list.pop()

    def size(self):
        return len(self.__stack_list)

if __name__ == "__main__":
    stack = stack_class()
    total_cnt = 0

    input_str = input()
    temp_pre = ''

    for each in input_str:
        if each is '(':
            stack.push(each)
        elif each is ')' and temp_pre is '(':
            stack.pop()
            total_cnt += stack.size()
        elif each is ')':
            stack.pop()
            total_cnt += 1
        temp_pre = each
    
    print(total_cnt)
