# x = int(input(""))

# vps = []
# value = []
# for i in range(x):
#     ps = input("")
#     array = list(ps)
#     if ps.count('(') == ps.count(')'): #( )개수 같아야 하는 조건
#         for j in range(len(array)):
#             if array[j]=='(':
#                 vps.append(array[j])
#             elif vps and array[j]==')':
#                 del vps[-1]
#             else:
#                 value.append("NO")
#                 break
#         if not vps: #When vps is NULL
#             if len(value)==i:
#                value.append("YES")

#     else:
#         value.append("NO")

# for i in range(len(value)):
#     print(value[i])


# case = int(input())
# result = []

# for i in range(case):
#     bracket = list(input())
#     bracket_stack = []
#     double_break = True

#     for j in range(len(bracket)):
#         if bracket[j] == "(":
#             bracket_stack.append(bracket[j])
#         else:
#             try:
#                 if bracket_stack.pop() == "(":
#                     pass
#             except:
#                 result.append("NO")
#                 double_break = False
#                 break

#     if len(bracket_stack):
#         result.append("NO")
#         continue

#     if double_break:
#         result.append("YES")


# for i in result:
#     print(i)
import sys

x = int(input(""))

vps = []
value = []
for i in range(x):
    ps = input("")
    array = list(ps)
    if ps.count('(') == ps.count(')'): #( )개수 같아야 하는 조건
        for j in range(len(array)):
            if array[j]=='(':
                vps.append(array[j])
            elif vps and array[j]==')':
                del vps[-1]
            else:
                value.append("NO")
                break
        if not vps: #When vps is NULL
            if len(value)==i:
               value.append("YES")

    else:
        value.append("NO")

for i in range(len(value)):
    print(value[i])
