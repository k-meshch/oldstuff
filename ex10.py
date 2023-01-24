name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()

#builds "histogram" for the amount of hours repeated after the key word 'From'
for line in handle:
    if line.startswith('From '):
        hour = line.split()[5].split(':')
        counts[hour[0]]=counts.get(hour[0],0)+1



lst=list()

#
for key, value in counts.items():
    lst.append( key,value )

for hour,counts in sorted(lst):
    print (hour,counts)
