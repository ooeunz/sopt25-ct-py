result = 1;
for each in range(3):
    result *= int(input())

number = [0 for i in range(10)]
for each in str(result):
    number[int(each)] += 1;
    
for i in number:
    print(i)
