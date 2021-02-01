def leap_year(year):
    '''Determine if the supplied year is a leap year.'''
    if not(year % 400):
        return True
    elif not(year % 100):
        return False
    elif not(year % 4):
        return True
    else:
        return False

lyears = [year for year in range(1979,2016) if leap_year(year)]
print(lyears)
