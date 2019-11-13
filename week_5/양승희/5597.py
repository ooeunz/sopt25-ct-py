# 과제 안내신 분..?

temp = [i for i in range(1,31)]

for idx in range(28):
    temp.remove(int(input()))

print("\n".join(map(str, temp)))
