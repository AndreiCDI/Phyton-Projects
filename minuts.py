



def minutes_in_words (my_time):
    
    
    minut_unit = {0: 'ноль', 1 : 'одна', 2 : 'две', 3 : 'три', 4 : 'четыре', 5 : 'пять',    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
    minut_dec = {10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок',   50 : 'пятьдесят'}
    minut_tw = {11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать',    14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать',    17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}
    minut = 'минут'

    my_time = int(my_time)

    if my_time>=0 and my_time<=59:
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

        if my_time <10:
            print (minut_unit[my_time], min_end (my_time, minut))
        elif my_time == 10 or my_time == 20 or my_time == 30 or my_time == 40 or my_time == 50:
            print (minut_dec[my_time], min_end (my_time, minut))
        elif my_time < 20:
            print(minut_tw[my_time], minut)
        elif my_time < 60:
            my_time = str(my_time)
            y0 = int(my_time[:1])*10
            y1 = int(my_time[1:])
            y3 = minut_dec[y0] + minut_unit[y1]
            print (y3, min_end (my_time[1:], minut))
    else: print ('Out of range!!!!')

minutes_in_words(input ('input number 0-59 ',))



    

