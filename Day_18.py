'''
Lefty keeps track of the length of each fish that he catches. Below are the lengths in
inches of the fish that he caught one day: 12, 13, 8, 10, 17 .
What is the largest fish lengths in inches of the fish that he caught one day?
Solve without using conditional statements and the loop.
'''

def largestFish(arr):
  arr.sort()
  arrayLength = len(arr)
  largestFishSize = arr[(arrayLength-1)]
  return largestFishSize

fishLengthArr = [12, 13, 8, 10, 17]
largestFishSize = largestFish(fishLengthArr)
print("Largest fish size = ",largestFishSize)
