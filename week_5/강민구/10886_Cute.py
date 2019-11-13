cute = {0:0, 1:0}
N = int(input())
for _ in range(N) :
    a = int(input())
    cute[a] += 1

print("Junhee is not cute!" if cute[0]>cute[1] else "Junhee is cute!")