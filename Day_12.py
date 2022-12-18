'''
The number of rred blood corpuscles in one the cubic millimetre is about 5000000 and the
number of white blood corpuscles in one cubic millimetre is about 8000. What then is the
ratio of wbc to rbc? Aspect ratio should be int value.
'''

def greatestCommonFactor(whiteC, redC):
  return whiteC if (redC == 0) else greatestCommonFactor(redC, whiteC % redC)

redCorpuscles = 5000000
whiteCorpuscles = 8000

factor = greatestCommonFactor(whiteCorpuscles, redCorpuscles)

whiteRatio = int(whiteCorpuscles / factor)
redRatio = int(redCorpuscles / factor)

print("Aspect Ratio: ",whiteRatio,":",redRatio)
