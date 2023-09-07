n=input("Enter the string:")
l1=[]
l2=[]
v=0
c=0
for i in n:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        v=v+1
        l1.append(i)
    
    else:
        c=c+1
        l2.append(i)
        
print("List of vowels:",l1)
print("List of other consanents:",l2)
