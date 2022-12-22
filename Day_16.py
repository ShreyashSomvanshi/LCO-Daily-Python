'''
Write a program to get the sum of n number. Ex sum of 123 is 6
'''

def getSum(n):
  tot = 0
  while n>0:
    dig = n%10
    tot = tot + dig
    n = n//10
  return tot

n = int(input("Enter a number: "))
sum_of = getSum(n)
print("The total sum of", n,"is:", sum_of)
