fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    separated=line.split()
    for word in separated:
        if word in lst: continue
        lst.append(word)

lst.sort()
print(lst)
