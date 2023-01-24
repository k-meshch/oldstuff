# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count = count + 1
        number = line.find('0')
        fullnum=float(line[number:])
        total=total+fullnum
avg=total/count

print("Average spam confidence:", avg)
