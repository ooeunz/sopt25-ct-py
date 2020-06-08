arr = [1,2,4]
result = list()
for i in range(int(input())):
    value = int(input())

    if len(arr) < value:
        for j in range(len(arr),value,1):
            arr.append(arr[j-3] + arr[j-2] + arr[j-1])
        print(arr[-1])
    else:
        print(arr[value-1])
