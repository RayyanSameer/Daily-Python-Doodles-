#This file is a password manager 

#It essentially works by validating your password against a set of requirements 
#if you meet a requirement you get 20 points if not , 0 points 
#it then validates it on a benchmark 
#This is a function based modular program 

required_length = 12
points = 0
password = []
target = ["!","@","#","%","^","&","*","(",")","+","-","/","{","}","[",",",":",";","|",]

#Check Len

def check_password_length(password):
    if len(password) >= required_length:   
        return points + 20
    elif len(password) >= 8:
        return points + 15
    else:
        return points 


#Check if uppercase

def check_is_upper(password):
    for p in password:
        if p.isupper():
            return 30 
    return 0 
        
#Check digits 

def is_digit(password):
    for p in password:
        if p.isdigit():
            return points + 20     
    else:
        return 0      

#Check signs 

def check_signs(password):
    for p in password:
        if p in target:
            return 20
    return 0
    
def get_verdict(score):
    if score >= 80:
        return "Strong"
    elif score >= 50:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    
    points = (
        check_password_length(password) +
        check_is_upper(password) +
        is_digit(password) +
        check_signs(password)
    )
    
    verdict = get_verdict(points)
    print(f"\nScore: {points}/100")
    print(f"Verdict: {verdict}")            
    
    

