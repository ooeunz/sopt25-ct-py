# -*- coding: utf-8 -*-

num_case = int(input())
for _ in range(num_case):
    detective = []
    suspect = input()
    alreadyDetected = False
    for key in suspect:
        if key == "(":
            detective.append(1)
        else:
            if len(detective) == 0:
                print("NO")
                alreadyDetected = True
                break
            detective.pop()
    
    if alreadyDetected == True:
        continue
    if len(detective) == 0:
        print("YES")
    else:
        print("NO")

