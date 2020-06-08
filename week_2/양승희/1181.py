# 정렬/ 백준 - 단어정렬
    
list = list()

for each in range(int(input())):
    str = input()
    if not str in list:
        list.append(str)

# 람다 (첫번 째 기준, 두번 째 기준)
list = sorted(list,key = lambda x: (len(x),x))

print("\n".join(list))