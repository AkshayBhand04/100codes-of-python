def leap_or_not(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        print("The entered",year,"year is leap year")
    else:
        print("The entered year is not a leap year")    



while True:
    year=int(input("Enter the year"))
    leap_or_not(year)