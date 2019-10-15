if __name__ == "__main__":
stack = list()
total_cnt = 0

input_str = input()
temp_pre = ''

for each in input_str:
    if each is '(':
        stack.append(each)
    elif each is ')' and temp_pre is '(':
        stack.pop()
        total_cnt += len(stack)
    elif each is ')':
        stack.pop()
        total_cnt += 1
    temp_pre = each

print(total_cnt)
