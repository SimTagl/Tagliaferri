import math

A= int(input("A:"))
B= int(input("B:"))
C= int(input("C:"))

if A>B and A>C:
    print("A is the greater")
elif B>A and B>C:
    print("B is the greater")
elif C>A and C>B:
    print("C is the greater")
else:
    print("A,B,C are the same number")
            
