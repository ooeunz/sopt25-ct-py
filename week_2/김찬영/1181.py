import operator
num = int(input())
list = []
dict = {}
for i in range(0,num):
    list.append(input())

for i in list:
    dict[i] = len(i)
dict = sorted(dict.items())
dict = sorted(dict,key=operator.itemgetter(1))
for i in range(0,len(dict)):
    print(dict[i][0])