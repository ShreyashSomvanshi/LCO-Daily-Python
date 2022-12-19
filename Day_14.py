'''
How many ways can four students Ram, Anuj, Deepak and Ravi line up in
a line, if the order matters? Print all possible combinations.
'''

def printAllCombinations(students):
  if len(students) == 0:
    return []
  
  if len(students) == 1:
    return [students]
  
  l = []
  for i in range(len(students)):
    m=students[i]
    remLst = students[:i] + students[i+1:]
    for p in printAllCombinations(remLst):
      l.append([m]+p)
  return l


studentArray = ["Ram", "Anuj", "Deepak", "Ravi"]

for combination in printAllCombinations(studentArray):
  print(combination)
