l=[2,4,1,3,5]
def sum(l):
    s=0
    i=0
    while i<len(l):
        s=s+l[i]
        i=i+1
    print("Sum of digits:",s)
sum(l)

