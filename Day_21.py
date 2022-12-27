'''
Write a program that for a given hour and minutes values calculates an
angle in degrees between the hour and the minute hands. Check whether the
minute hand overlapping the hour hand at a given time.
'''

def calcAngle(h,m):
  if(h<0 or m<0 or h>12 or m>60):
    print("Wrong input")
    
  if(h==12):
    h=0
  if(m==60):
    m=0
  hourAngle = 0.5*(h*60+m)
  minuteAngle = 6*m
  angle = abs(hourAngle - minuteAngle)
  angle = min(360 - angle, angle)
  return int(angle)

h = int(input("Enter hour(1-12): "))
m = int(input("Enter minutes(0-59): "))
clockAngle = calcAngle(h,m)
if clockAngle == 0:
  print("hour and minute hands overlaps")
else:
  print(clockAngle,"degree")

