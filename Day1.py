# There was a teacher in small town who loves coding and he wants to create a program
# which prints out whole multiplication table of an entered number for his students. Can you help
# him to write a program in python?

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)

