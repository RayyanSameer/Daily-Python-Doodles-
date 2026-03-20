#PSUDOCODE
#Get a secret number from 1 to 100 via randint 
#Allot 7 Guesses 
#WHile the number of guesses < tries 
#if guess ==  secret , win
#if guess > secret , highelse low 

#Keep a score , low guesses 100 , every guess costs 15

max_guesses = 7 

import random 

def calculate_score(attempts):
    score = 100 - ((attempts - 1) * 15)
    return max(score,0)

def play_round():
    secret = random.randint(1,100)
    attempts = 0

    while attempts < max_guesses:
        try:
            guess = int(input(f"Guess ({max_guesses - attempts} left): "))
        except ValueError:
            print("Pls enter a number: ")
            continue

        attempts += 1
        if guess == secret:
            
            current_score = calculate_score(attempts)
            print(f"Correct! Attempts: {attempts} | Score: {current_score}")
            return current_score
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of guesses. The number was {secret}.")
    return 0 

if __name__ == "__main__":
    print("=== Number Guessing Game ===\n")
    
    total_score = 0
    rounds = 3 
    
    for i in range(rounds):            
        print(f"\n--- Round {i+1} ---")
       
        round_result = play_round()
        total_score += round_result 
    
    print(f"\nFinal Score: {total_score} / {rounds * 100}")