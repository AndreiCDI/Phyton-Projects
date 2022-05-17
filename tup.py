
db = {9103976271:("Reina Meinhard", "Memphis", "Tennessee"),
    4199392609:("Stephanie Bruce", "Greensboro", "North Carolina"),
    9099459979:("Ermes Angela", "Dallas", "Texas"),
    6123479367:("Lorenza Takuya", "Indianapolis", "Indiana"),
    7548993768:("Margarete Quintin", "Raleigh", "North Carolina")}

x = int(input("input number"))
#if x in db:
#    print (f'{db[x][0]} from {db[x][1]}, {db[x][2]}')
#else :
#    print ('the num not found')
val = db.get(x)
if val:
    print(val[0], "from", val[1], val[2])
else:
    print ('the num not found')
    
