arr = [1,2]
result = list()

value = int(input())

if len(arr) < value:
    for i in range(len(arr),value):
        arr.append((arr[i-2] + arr[i-1])%15746)
    print(arr[-1])
else:
    print(arr[value-1])