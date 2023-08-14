#Program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

year = int(input("Which year do you want to check? "))

#Solution 1

isDivisibleBy4 = year % 4
isDivisibleBy100 = year % 100
isDivisibleBy400 = year % 400

if isDivisibleBy4 == 0 and isDivisibleBy100 == 0 and isDivisibleBy400 == 0:
    print("Leap year.")
elif isDivisibleBy4 == 0 and isDivisibleBy100 > 0 and isDivisibleBy400 > 0:
    print("Leap year.")
elif isDivisibleBy4 > 0 and isDivisibleBy100 > 0 and isDivisibleBy400 == 0:
    print("Leap year.")
elif isDivisibleBy4 == 0 and isDivisibleBy100 > 0 and isDivisibleBy400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")


#Solution 2

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# NOTES

# This is how you work out whether if a particular year is a leap year
# On every year that is evenly divisible by 4 
# Except every year that is evenly divisible by 100 
# Unless the year is also evenly divisible by 400