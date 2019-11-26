min_num=[sum(int(plus) for plus in minus.split('+')) for minus in input().split('-')]
print(min_num[0] - sum(min_num[1:]))