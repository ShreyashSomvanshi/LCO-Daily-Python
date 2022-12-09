# The city's bus system carries 1,200,000 people each day. How many people does the bus
# system carry each year? (1 yr = 365 days). Solve without using *,/ operators, bitwise operator or loop

# Solution:

def multiply(x,y):
  if(y==0):
    return 0
  if(y>0):
    return (x+multiply(x,y-1))
  if (y<0):
    return -multiply(x,-y)
  
peopleTravelDaily = 1200000
daysofyear = 365
peopletravelYearly = multiply(peopleTravelDaily, daysofyear)

print(peopletravelYearly)
