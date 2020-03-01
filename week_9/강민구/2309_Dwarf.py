import sys

dwarfs = list(sys.stdin.readline().strip() for _ in range(9)) #난쟁이들의 키를 담은 리스트 생성
dwarfs = list(map(int,dwarfs))
weight = sum(dwarfs)
check = False
for i in range(len(dwarfs)) :
    dwarf_1 = dwarfs[i]
    for j in range(len(dwarfs)):
        dwarf_2 = dwarfs[j]
        if i == j : # 드워프 탐색 중복 방지
            continue
        else :
            if weight - (dwarf_1 + dwarf_2) == 100 :
                dwarfs.remove(dwarf_1)
                dwarfs.remove(dwarf_2)
                check = True
                break
    if check == True :
        break
dwarfs.sort()
for dwarf in dwarfs :
    print(dwarf)