p,w = input().split(" ")
p = int(p)
w = int(w)
result = 0
first = ['A','D','G','J','M','P','T','W',' ']
second = ['B','E','H','K','N','Q','U','X']
third = ['C','F','I','L','O','R','V','Y']
fourth = ['S','Z']
message = list(input())
slack = "null"
for i in message:
    if slack is "first":
        if i in first:
            result = result + p + w
            if i is ' ':
                slack = "blank"
            else:
                slack = "first"
        elif i in second:
            result = result + 2*p
            slack = "second"
        elif i in third:
            result = result + 3*p
            slack = "third"
        elif i in fourth:
            result = result + 4*p
            slack = "fourth"
    elif slack is "second":
        if i in first:
            result = result + p
            if i is ' ':
                slack = "blank"
            else:
                slack = "first"
        elif i in second:
            result = result + 2*p + w
            slack = "second"
        elif i in third:
            result = result + 3*p
            slack = "third"
        elif i in fourth:
            result = result + 4*p
            slack = "fourth"
    elif slack is "third":
        if i in first:
            result = result + p
            if i is ' ':
                slack = "blank"
            else:
                slack = "first"
        elif i in second:
            result = result + 2*p
            slack = "second"
        elif i in third:
            result = result + 3*p + w
            slack = "third"
        elif i in fourth:
            result = result + 4*p
            slack = "fourth"
    elif slack is "fourth":
        if i in first:
            result = result + p
            if i is ' ':
                slack = "blank"
            else:
                slack = "first"
        elif i in second:
            result = result + 2*p 
            slack = "second"
        elif i in third:
            result = result + 3*p
            slack = "third"
        elif i in fourth:
            result = result + 4*p + w
            slack = "fourth"
    else:
        if i in first:
            result = result + p
            if i is ' ':
                slack = "blank"
            else:
                slack = "first"
        elif i in second:
            result = result + 2*p 
            slack = "second"
        elif i in third:
            result = result + 3*p
            slack = "third"
        elif i in fourth:
            result = result + 4*p
            slack = "fourth"
    print(result)    
print(result)