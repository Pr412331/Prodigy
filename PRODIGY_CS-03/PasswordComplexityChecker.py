#!/usr/bin/env python
# coding: utf-8

# In[6]:


def isStrong(password):
    if len(password) < 12:
        return "Password strength is week. Can be cracked easily."
        
    oneUpper = any(char.isupper() for char in password)
    oneLower = any(char.islower() for char in password)
    oneDigit = any(char.isdigit() for char in password)
    special = "!@#$%^&*()-_+=<>,.?/:;{}[]|~"
    oneSpecial = any(char in special for char in password)
    
    if (oneUpper and oneLower and oneDigit and oneSpecial):
        return "Password strength is Strong. Hard to crack it."
        
    elif (oneUpper or oneLower or oneDigit or oneSpecial):
        return "Password strength is Medium. Can be cracked."
        
    else:
        return "Password strength is week. Can be cracked easily."

def main():
    print("Password should meet the following requirements")
    print("Length should be greater than 12 characters.")
    print("Lowercase Characters")
    print("Uppercase Characters")
    print("Digits")
    print("Special Characters")
    password = input("Enter the password: ")
    print("Strength: ", isStrong(password))
    

if __name__ == "__main__":
    main()


# In[ ]:




