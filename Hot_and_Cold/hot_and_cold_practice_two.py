#Psudocode 

#Allot 7 guesses 
#Keep a score tag eavh guess costs 15 points 
#Allot a random secret number 
#while guess < allowed :
#if < secret "Low"
#if > secret "High You have {guesses} remaining"
#if == secret "Right with {insert tries}"

import random
max_guesses = 7



def calculate_score(attempts):
    score = 100 - ((attempts - 1) * 15)
    return max(score,0)


def play_round():
    secret = random.randint(0,100)
    attempts = 0
    while attempts < max_guesses:
        try:
            guess = int(input("Guess a number "))
            attempts +=1
        except ValueError:
            print("Enter a number !") 
            continue   
        if guess == secret:

            current_score = calculate_score(attempts)
            print(f"Correct|Score: {current_score}")
            return current_score

            
        elif guess < secret:
            print(f"Too low . you have {max_guesses - attempts} remaining")   
        else:
            print(f"Too high . you have {max_guesses - attempts} remaining")
    print(f"Out of guesses the answer was {secret}")
    return 0

if __name__=="__main__":
    print("___NUMBER GUESSING GAME___")
    rounds = 3
    total_score = 0

    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
       
        round_result = play_round()
        total_score += round_result 
    
    print(f"\nFinal Score: {total_score} / {rounds * 100}")


