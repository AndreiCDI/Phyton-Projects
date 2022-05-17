my_time = str(input("Inter time in format hh:mm  "))
x = my_time.split(':')
s = x[1]
print (s[1:])
minut = 'минут'

def min_end (min_index, mi):
    min_index = int(min_index)
    if min_index == 1:
        mi = mi + 'а'
        return (mi)
    elif min_index == 2 or min_index == 3 or min_index == 4:
        mi = mi + 'ы'
        return (mi)
    else:
        return (mi)

print (min_end (s[1:], minut))


#min_index =int(x[1])
#print (min_index)