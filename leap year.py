# if a number is by 4 and not divisible by 100 then it is a leap year
#if it is divisible by 400 then it is a leap year 

year= int(input(" check which year is leap year? "))
if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")
    