A=float(input("ENTER THE LENGTH OF SIDE 1 = "))
B=float(input("ENTER THE LENGTH OF SIDE 2 = "))
C=float(input("ENTER THE LENGTH OF SIDE 3 = "))
if(A == B and A == C):
    print("the triangle is isolateral")
elif(A == B or B == C or A == C):
    print("the triangle is isoscale")
else:
    print("the triangle is isolene")
