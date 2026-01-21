import os 
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

passwd = input("Enter a password : ")
passwd_confirm = input("Enter password again: ")

def process_and_save(passwd_text):
  
    encoded_passwd = passwd_text.encode("UTF-8")
    
    
    encrypted_passcode = cipher_suite.encrypt(encoded_passwd)
    
   
    with open("passcodes.bin", "wb") as file:
        file.write(encrypted_passcode)
    
    print("Passwords encrypted and saved to passcodes.bin")

if passwd == passwd_confirm:
    print("Passwords are a match!")
    process_and_save(passwd)
else:
    print("Not matching!")
