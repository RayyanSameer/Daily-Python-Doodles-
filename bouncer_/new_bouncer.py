class ClubError(Exception):
    #base 
    pass

class UnderAgeError(ClubError):
    pass

class BannedError(ClubError):
    pass

class KeyError(ClubError):
    pass

#Brain
def checkguest(guest_data):
        
            #ID_CHECK
    name = guest_data['name']
    age = guest_data['age']
    if age < 18:
        raise UnderAgeError(f"Sorry , too young ")     
    if name == "Joker":
        raise BannedError(f"Banned")
    
    return f"Welcome {name}"
    
# i/O
def process (queue):
    for guests in queue:
        try:
            result = checkguest(guests)
            print(result)

        except UnderAgeError as e:
            print(f" REJECTED (Age): {e}")
            
        except BannedError as e:
            print(f" POLICE CALLED: {e}")
            
        except KeyError:
            print(f"  ERROR: Guest forgot their ID (Data missing).")
            
        except Exception as e:
            print(f" UNKNOWN ERROR: {e}")

if __name__ == "__main__":
    # The Line outside the club
    line = [
        {"name": "Bruce", "age": 35},       # Valid
        {"name": "Robin", "age": 16},       # UnderageError
        {"name": "Joker", "age": 45},       # BannedGuestError
        {"name": "Ghost"},                  # KeyError (Missing age)
        {"name": "Tony", "age": 25}         # Valid
    ]
    
    process(line)            


        