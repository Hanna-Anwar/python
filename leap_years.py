# leap_year(year):

# if year%400 == 0 and year%100 ==0  or year%100!=0 and year%4==0:
  
#  return  year
    



# year = int(input("enter a year:"))

# res = leap_year(year)

# print("leap year",year)
 

year = int(input("enter a year"))

if year%100 == 0 and year%400 ==0  or year%100!=0 and year%4==0:

    print(f"{year} is leap year")

else:

     print(f"{year} is not a leap year")


# for year in range(2000,2051):
     
#     if year%100 == 0 and year%400 ==0  or year%100!=0 and year%4==0:
    
#       print(year)
     


