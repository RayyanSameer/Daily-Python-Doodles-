#This is a moduar program to check if a given password is meeting a set of requirements 

#it takes a password and runs a check on it's length , digit , symbols 
##This is a moduar program to check if a given password is meeting a set of requirements 

#it takes a password and runs a check on it's length , digit , symbols 


required_length = 12
target = ["!","@","#","%","^","&","*","(",")","+","-","/","{","}","[",",",":",";","|",]


def check_length(password):
    if len(password) >= required_length:
        return 20
    elif len(password) >= 8:
        return 15
    return 0

def check_upper(password):
    for p in password:
        if p.isupper():
            return 30
    return 0 

def check_digits(password):
    for p in password:
        if p.isdigit():
            return 20
    return 0

def check_symbols(password):
    for p in password:
        if p in target:
            return 30
    return 0

def get_verdict(score):
    if score >= 90:
        return "Strong"
    elif score >= 50:
        return "Moderate"
    else:
        return "Weak"
    
if __name__ == "__main__":
    
    user_password = input("Enter a password to check: ")

   
    calculated_points = (
        check_length(user_password) +
        check_upper(user_password) +
        check_digits(user_password) +
        check_symbols(user_password)
    )

  
    verdict_string = get_verdict(calculated_points)

   
    print(f"\nScore: {calculated_points}/100")
    print(f"Verdict: {verdict_string}")




required_length = 12
target = ["!","@","#","%","^","&","*","(",")","+","-","/","{","}","[",",",":",";","|",]


def check_length(password):
    if len(password) >= required_length:
        return 20
    elif len(password) >= 8:
        return 15
    return 0

def check_upper(password):
    for p in password:
        if p.isupper():
            return 30
    return 0 

def check_digits(password):
    for p in password:
        if p.isdigit():
            return 20
    return 0

def check_symbols(password):
    for p in password:
        if p in target:
            return 30
    return 0

def get_verdict(score):
    if score >= 90:
        return "Strong"
    elif score >= 50:
        return "Moderate"
    else:
        return "Weak"
    
if __name__ == "__main__":
    
    user_password = input("Enter a password to check: ")

   
    calculated_points = (
        check_length(user_password) +
        check_upper(user_password) +
        check_digits(user_password) +
        check_symbols(user_password)
    )

  
    verdict_string = get_verdict(calculated_points)

   
    print(f"\nScore: {calculated_points}/100")
    print(f"Verdict: {verdict_string}")


