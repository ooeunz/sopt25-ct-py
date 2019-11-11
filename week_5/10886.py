count = int(input())
one_count = 0
zero_count = 0
for _ in range(count):
    if(input()=='1'):
        one_count = one_count + 1
    else:
        zero_count = zero_count + 1
if(one_count>zero_count):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")