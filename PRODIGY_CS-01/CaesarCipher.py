def CaesarEncrypt(text, shift):
    enc = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                enc += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                enc += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            enc += char
    return enc

def CaesarDecrypt(encrypted_text, shift):
    dec = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                dec += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                dec += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            dec += char
    return dec

text = input("Enter the string: ")
s = eval(input("Enter the shifting number: "))
print("\n")
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + CaesarEncrypt(text,s))

cipher = CaesarEncrypt(text, s)
print ("Original: " + CaesarDecrypt(cipher,s))




