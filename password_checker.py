# Password strength Checker

import re

def check_password_strength(password):
    if len(password) <8:
          return "weak: Password must be at least 8 chars"
      
    if not any(char.isdigit()for char in password):
          return "weak: password must contain a digit"
      
    if not any(char.isupper()for char in password):
     return "weak:password must contain an upper char"
 
    if not any(char.islower()for char in password):
     return "weak: password must contain an lower char"
 
    if not re.search(r'[@#$%^&*?:<>,.{}]', password):
     return "medium: Add special characters to make your password stronger."

    return "Strong: Your password is Secure!"

def password_checker():
    print("Welcome to the password Strength Checker")
    

    while True:
       password = input("Enter Your password (or type'exit'to quit):")
       if password.lower() == 'exit':
           print("Thank you using this Tool")
           break
       result = check_password_strength(password)
       print(result)
    
    
    
    
    #Run the Password Checker tool
if __name__ == "__main__":
      password_checker()
        
       

 
    