cnt = 0

for i in range(int(input())):
    str_list = list()
    check = True

    for i in input():
        if i in str_list:

            if str_list[-1] == i:
                continue

            check = False
            break
            
        else:
            str_list.append(i)
    
    print(str_list)
    print(check)
    if check == True:
        cnt += 1
    
print(cnt)
