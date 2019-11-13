postfix = []
operator = []

def solution(prefix):
    for i in prefix:
        if i is '(':
            operator.append(i)
        elif i is ')':
            while operator and operator[-1] is not '(':
                postfix.append(operator.pop())
            operator.pop()
        elif i is '+' or i is '-':
            if not operator or operator[-1] is '(':
                operator.append(i)
            else:
                postfix.append(operator.pop())
                operator.append(i)
        elif i is '*' or i is '/':
            if (operator and (operator[-1] is '+' or operator[-1] is '-')) or not operator:
                operator.append(i)
            else:
                postfix.append(operator.pop())
                operator.append(i)
        else:
            postfix.append(i)
    while operator:
        postfix.append(operator.pop())
    print(''.join(postfix))

if __name__ == "__main__":
    prefix = list(input())
    solution(prefix)