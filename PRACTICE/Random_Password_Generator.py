#Password Generator 

#Ask length , special charecter (y/n) , uppercase? (y/n), digits? (y/n)

#Get all available charecters
#Randomly pick upto length
#Have one min type of charecter
#Ensure valid length

import random
import string

def gen_passwd():
    length = input("Enter the desired length: ").strip()
    include_uppercase = input("Include uppercase? (Y/N): ")
    include_lowercase = input("Include lowercase? (Y/N): ")
    include_special = input("Include special-case? (Y/N): ")
    include_digit  = input("Include digits ? (Y/N): ")

    if length  < 4 :
        print("Password must have a charecter count higher than four ")
        return
    
    lower = string
    
