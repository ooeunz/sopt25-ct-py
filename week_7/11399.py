count = int(input())
list_BankTime = input().split(" ")
list_BankTime = list(map(int,list_BankTime))
list_BankTime.sort()
result = 0
flag_result = 0
for i in range(count):
    flag_result = flag_result + list_BankTime[i]
    result = result + flag_result
print(result)