# On a certain day, the nurses at a hosppital worked the following number of hours: Nurse Howard worked 8 hours; Nurse Pease worked 10 hours;
# Nurse Campbell worked 9 hours; Nurse Grace worked 8 hours; Nurse McCarthy worked 7 hours, and Nurse Murphy worked 12 hours. What is the average 
# number of hours worked per nurse on this day?
# Average should be as a float value.

# Solution:

def avgWork(a,b,c,d,e,f,nCount):
  totalHrs = float(a+b+c+d+e+f)
  temp = float(totalHrs + nCount)
  avgHrs = totalHrs/nCount
  
  return avgHrs

nHoward = 8
nPease = 10
nCampbell = 9
nGrace = 8
nMcCarthy = 7
nMurphy = 12
nurseCount = 6

avghours = avgWork(nHoward,nPease,nCampbell,nGrace,nMcCarthy,nMurphy,nurseCount)

print("Average Hours is", avghours)
