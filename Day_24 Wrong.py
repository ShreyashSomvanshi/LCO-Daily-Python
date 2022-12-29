'''
If julius has j books and Nancy has n. How many books do they have altogether?
Convert and print as an Roman number. j,n are user entered values.
'''

num_map = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def num2roman(num):
  roman=''
  while num>0:
    for i,r in num_map:
      while num>=1:
        roman+=r
        num-=i
  return roman

jBooks = int(input("Enter Julius's Book Count: "))
nBooks = int(input("Enter Nancy's Book Count: "))
value = jBooks + nBooks
rn = num2roman(value)
print(value,'--->',rn)
