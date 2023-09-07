def triangle(a,b,c):
    if(a**2==b**2+c**2)and(b**2==a**2+c**2)and(c**2==a**2+b**2):
        print("It is a right angle triangle.")
    else:
        print("It is not a right angle triangle.")
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
triangle(a,b,c)