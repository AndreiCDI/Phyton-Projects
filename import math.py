import math

a = float ( input ("Input a "))
b = int (input ("Input b "))
c = int (input ("Input c "))
d = b**2-4*a*c
print (d)
if d>0:
    x1=-b + math.sqrt(D)/2*a
    x2=-b - math.sqrt(D)/2*a
    print (d)
    print (x1)
    print (x2)
elif d == 0:
     x=-b/2*a
     print (x)
    
else:
    print ("no solution")

  
