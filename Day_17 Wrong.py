'''
There are 10 students in a class, some students names are same to other students,
print the names that occur more than one time. All names should be in a single string.
Ex: str="Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vandh Rajat Sagar"
'''

def printStringDuplicate(studentName):
  x = studentName.split()
  _size = len(x)
  repeated = []
  
  for i in range(_size):
    k = i + 1
    for j in range(k, _size):
      if x[i] == x[j] and x[i] not in repeated:
        repeated.append(x[i])
        print(x[i])
        
students = "Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vandh Rajat Sagar"
printStringDuplicate(students)
