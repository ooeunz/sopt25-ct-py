vertical,horizontal = input().split(" ")
vertical = int(vertical)
horizontal = int(horizontal)
candy = [[0]*horizontal for i in range(vertical)]
result = [[0]*horizontal for i in range(vertical)]
for v in range(vertical):
    a = input().split(" ")
    for h in range(horizontal):
        candy[v][h] = int(a[h])
for v in range(vertical):
    for h in range(horizontal):
        if(v==0 and h==0):
            result[v][h] = candy[v][h]
        elif((v==1 and h==0) or (v==0 and h==1)):
            result[v][h] = candy[v][h] + candy[0][0]
        elif(v==0):
            result[v][h] = candy[v][h] + result[v][h-1]
        elif(h==0):
            result[v][h] = candy[v][h] + result[v-1][h]
        else:
            big = max(result[v-1][h],result[v][h-1],result[v-1][h-1])
            result[v][h] = candy[v][h] + big
print(result[v][h])