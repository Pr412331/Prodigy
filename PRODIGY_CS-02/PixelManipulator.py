#!/usr/bin/env python
# coding: utf-8

# In[1]:


from colorama import Fore


# In[2]:


def encrypt_image(path, key):
    try:
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()

        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()

        print(Fore.GREEN + "Encryption Done...")
        print(Fore.GREEN + "Exiting...")
        
    except Exception:
        print(Fore.RED + "Error caught : ", Exception.__name__)
        print(Fore.RED + "Exiting...")
        

def decrypt_image(path, key):
    try:
        fin = open(path, 'rb')
        image = fin.read()
        image = bytearray(image)
        
        for index, value in enumerate(image):
            image[index] = value ^ key
            
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        
        print(Fore.GREEN + "Decryption Done...")
        print(Fore.GREEN + "Exiting...")
        
    except Exception:
        print(Fore.RED + "Error caught : ", Exception.__name__)
        print(Fore.RED + "Exiting...")
        

filePath = input('Enter path of Image : ')
key = int(input('Enter Key for encryption of Image : '))
print('The path of file : ', filePath)
print('Key for encryption : ', key)

while True:
    print("\nPixel Manipulator for Image Encryption/Decryption")
    print("\n1. Encryption")
    print("\n2. Decryption")
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        encrypt_image(filePath, key)
        break
        
    elif choice == 2:
        decrypt_image(filePath, key)
        break
        
    else:
        print(Fore.YELLOW + "\nInvalid option.")
        print(Fore.RED + "Exiting...")
        break


# In[ ]:




