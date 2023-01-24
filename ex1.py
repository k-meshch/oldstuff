hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate: ")
r = float (rate)

if h <=40:
    print (h*r)
elif h > 40:
    newrate=float(1.5*r)
    print (40*r + (h-40)*newrate)
