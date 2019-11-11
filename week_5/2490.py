for _ in range(3):
    count = 0
    temp = input().split()
    for i in temp:
        if(i == '0'):
            count = count + 1
    if count==0:
        print("E")
    elif count==1:
        print("A")
    elif count==2:
        print("B")
    elif count==3:
        print("C")
    elif count==4:
        print("D")