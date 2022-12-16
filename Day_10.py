'''
Salesperson Rita drives 2,052 miles in 6 days, stopping at 2 towns
each day. How many kilometers does she average between stops?
'''

totalMilesToDrive = 2052
totalDays = 6
townToStopPerDay = 2
kmPerMile = 1.60934

avgMiles = (totalMilesToDrive / totalDays) / townToStopPerDay

# conv miles to km
avgKM = avgMiles * kmPerMile

print("She drive average of",avgKM,"km between every stop.")
