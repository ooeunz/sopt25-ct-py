# 1904 - 01타일

# 1 , 00(이게 한쌍)
# n = 1 / 1
# n = 2 / 00,11
# n = 3 / 001,100,111
# n = 4 / 0011, 0000, 1001, 1100, 1111

# 1,2,3,5,8 <<피보나치네, % 15746



import sys
n = int(sys.stdin.readline())
a = 1
b = 2
cnt = 0
for i in range(n - 1):
    cnt = a
    a = b
    b = (cnt + b) % 15746
print(a)