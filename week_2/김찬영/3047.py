num = input().split()
num = list(map(int, num))
num.sort()
dict = {}
dict["A"] = num[0]
dict["B"] = num[1]
dict["C"] = num[2]
token = input()
for i in token:
    print(dict[i])