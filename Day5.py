# During the last week of track training. Shoshanna achieves the following times in sec-rounds: 66,57,54,53,64,52 and 59.
# Find her best score using bubble sort:

sec = [66,57,54,53,64,52,59]
n=len(sec)
for i in range(n):
    for j in range(0,n-i-1):
        if sec[j] > sec[j+1]:
            sec[j],sec[j+1] = sec[j+1],sec[j]
            
print("best time is",sec[0],"seconds")


