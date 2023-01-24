name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d=dict()

for line in handle:
    words= line.split()
    if 'From'in words:
        person=words[1]
        d[person]=d.get(person,0)+1

holder = 0
keyr= None
valuer = None
for key,value in d.items():
    if value > holder:
        holder = value
        keyr=key
        valuer=value
print (keyr, valuer)
