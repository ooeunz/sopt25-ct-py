ip = [int(input()) for _ in range(int(input()))]

calc = [-1]*12

def proc(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    if calc[n] != -1:
        return calc[n]
    calc[n] = proc(n-1)+proc(n-2)+proc(n-3)
    return calc[n]

print('\n'.join([str(proc(n)) for n in ip]))