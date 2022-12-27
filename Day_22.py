'''
Write a program to find if a given year is a Leap year or not.
'''

year = int(input("Enter a year: "))
flag = False
if(year % 4)==0:
  if(year%100)==0:
      if(year%400)==0:
        flag = True
      else:
        flag = False
  else:
    flag = True
else:
    flag = False
  
if(flag):
  print("Year", year, "is a leap year.")
else:
  print("Year", year, "is not a leap year.")
