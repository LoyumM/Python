def is_leap(year):
    leap = False
    
    if 1900<=year<=10**5:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap = True
    else:
        print("Year out of constraints.")
               
    return leap

    

year = int(input())
print(is_leap(year))