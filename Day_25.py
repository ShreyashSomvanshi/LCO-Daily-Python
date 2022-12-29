'''
Write a python method to check whether a string is a valid password.
Password rules:-
  * Should have atleast one number.
  * Should have atleast one uppercase and one lowercase character.
  * Should have atleast one special symbol.
  * Should be between 6 to 20 characters long.
'''

def chechPass(passwd):
    special_symbols = ['$','#','@','%']
    val = True
    if (len(passwd) < 6) or (len(passwd) > 20):
        print(" Password should be between 6 to 20 characters long.")
        val = False
        
    if not any(char.isdigit() for char in passwd):
        print("Password must have at least one numeral.")
        val = False
        
    if not any(char.isupper() for char in passwd):
        print("Password must have at least one uppercase letter.")
        val = False
        
    if not any(char.islower() for char in passwd):
        print("Password must have at least one lowercase letter.")
        val = False
        
    if not any(char in special_symbols for char in passwd):
        print("Password must have at least one of the $ # @ %")
        val = False
        
    if val:
        return val
    
password = input("Enter password: ")
if (chechPass(password)):
    print("Password is valid.")
    
else:
    print("Invalid Password")
  
