expression = input()
start = 0
end = 0
result = 0
number = []
giho = ['+',]
for i in range(len(expression)):
    if(expression[i]=='+' or expression[i]=='-'):
        number.append(expression[start:end])
        start = i + 1
        giho.append(expression[i])
    elif(i is (len(expression)-1)):
        end = i + 1
        number.append(expression[start:end])
    else:
        end = i + 1
number = list(map(int,number))
for i in range(len(number)):
    if(giho[i]=='+'):
        result = result + number[i]
    else:
        for j in range(i,len(number)):
            result = result - number[j]
        break
print(result)