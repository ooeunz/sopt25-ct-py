# 0 = not cute / 1 = cute

is_cute = [0,0]

for _ in range(int(input())):
    is_cute[int(input())] += 1

if is_cute[0] > is_cute[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")