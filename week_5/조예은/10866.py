# 다수결

person = int(input())
opiList = list()
for _ in range(person):
    opinion = int(input())
    opiList.append(opinion)

if opiList.count(1) < opiList.count(0):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')