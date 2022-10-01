print("Enter the year to check whether it is leap year or not:")
year = int(input())
if (year % 400 == 0) and (year % 100 == 0): #added century year condition as previios logic was wrong for century year
    print(year,"is a leap year")
elif( year % 4 == 0) and (year%100!=0):
    print (year,"is a leap year.")
else:
    print (year,"isn't a leap year.")
