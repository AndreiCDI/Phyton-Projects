eq_val = input("inter eq y = kx + b ")
x = input("input x ")


eq_val = eq_val.replace(" ",'').replace('y=','')
c = eq_val.split('x')
a = int(c[0])
b = int(c[1])
res = a*int(x) +b
print (a, b)
print (res)




