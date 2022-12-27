'''
Fin the square of the number without using Multiplication and Division operator.
'''
def square(n):
  sum = 0
  for i in range(0,n):
    sum = sum + n
  return sum

print(square(10))
