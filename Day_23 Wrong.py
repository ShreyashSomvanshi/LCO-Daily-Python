'''
Write a python program to convert integer values into binary. 
'''
def decToBin(val):
  bin_value = ''
  while val!=1:
    bin_value += str(val%2)
    val = val/2
  return '1'+bin_value[::-1]

n=int(input("Enter a no.: "))
b=decToBin(n)
print('binary',b)
