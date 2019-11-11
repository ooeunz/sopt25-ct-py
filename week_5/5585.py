change = 1000 - int(input())
count = 0
value = [500,100,50,10,5,1]
while(change is not 0):
    for i in value:
        if(change/i>=1):
            count = count + 1
            change = change - i
            break
print(count)