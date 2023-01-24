import re
hand=open('regex_sum_1044755.txt')
numlist=list()
total=0

for line in hand:
    line=line.rstrip()
    allnums=re.findall('[0-9]+',line)
    if len(allnums) < 1 : continue
    for num in allnums:
        numlist.append(int(num))

print(sum(numlist))
