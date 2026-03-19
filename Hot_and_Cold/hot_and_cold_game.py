# Game loop logic is the cleanest isolated test of whether you can manage state across multiple iterations  a skill backend and DevOps engineers use constantly in retry loops, polling scripts, and event processors. Interviewers use games to strip away framework knowledge and see raw logic

#Random number 1–100. 
# Player gets 7 guesses. 
# Each guess gets "too high" / "too low" feedback. 
# Game tracks guess count. Prints final score when done

import random

def play_game():
    secret = random.randint(1,100)
    guesses_allowed = 7
    attempts = 0

    while attempts < guesses_allowed:
        guess = int(input("Guess a number : "))
        attempts +=1

        if guess == secret:
            print(f"Correct! Got it in {attempts} guesses.")
        elif guess < secret:
            print("Too low")
        else:
            print("too high")

    print(f"Out of guesses. The number was {secret}.")

if __name__ == "__main__":
    play_game()                    