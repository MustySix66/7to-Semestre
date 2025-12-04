meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def dayOfYear(date):
    month, day, year = map(int, date.split('/'))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        # Si es bisiesto
        meses[1] = 29
        for i in range(month - 1):
            day += int(meses[i])
        return day
    else:
        meses[1] = 28
        for i in range(month - 1):
            day += int(meses[i])
        return day

print(dayOfYear("12/13/2020"))
# output = 348

print(dayOfYear("11/16/2020"))
# output = 321

print(dayOfYear("1/9/2019"))
# output = 9

print(dayOfYear("3/1/2004"))
# output = 61

print(dayOfYear("12/31/2000"))
# output = 366 # leap year
print(dayOfYear("12/31/2019"))
# output = 365 #non leap year