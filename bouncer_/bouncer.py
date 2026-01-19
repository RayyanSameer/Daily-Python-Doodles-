#Layer one : Here lay the custom exceptions 

class CLubError(Exception):
    "Base error class"
    pass

class UnderageError(CLubError):
    "Guest is too young"
    pass

class BannedError(CLubError):
    "Blacklisted"
    pass

#Layer two: The Brain

def check_guest(guest_data):
    #CheckID
    age = guest_data['age']
    name = guest_data['name']

    if age < 21:
        raise UnderageError(f"Sorry {name}, you are {age}. Come back when you are older")
    if name == "Joker":
        raise NameError(f"You have been banned ")
    return f"welcome {name}"

#Layer three : The I/O Layer 

def process_line(queue):

    for guest in queue:
        try:
        #Attempt to letem in
            result = check_guest(guest)
            print(f"{result}")
        except UnderageError as e:
            print(f"REJECTEDm (AGE): {e}")
        except NameError as e:
            print(f"SECURITY CALLED: {e}")
        except KeyError:
            print(f"DATA MISSING")
        except Exception as e:
            print(f"UNKNOWN {e}")


#Data

if __name__ == "__main__":
    line = [{"name": "Bruce", "age": 35},       # Valid
        {"name": "Robin", "age": 16},       # UnderageError
        {"name": "Joker", "age": 45},       # BannedGuestError
        {"name": "Ghost"},                  # KeyError (Missing age)
        {"name": "Tony", "age": 25}]    
    process_line(line)        

                  
