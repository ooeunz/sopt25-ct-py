sum = 0 
for _ in range(5):
    temp = int(input())
    if(temp<40):
        temp = 40
    sum = sum + temp
print(int(sum/5)) 