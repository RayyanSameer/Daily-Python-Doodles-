#List of common words to vey if this is english

common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "it","for", "not", "on", "with", "he", "as", "you", "do", "at", "this"]

#Encode FUnc

def encode(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            shifted = (ord(char) - base + shift) % 26 + base
            result =+ chr(shifted)
        else:
            result =+char
    return result


def decode(text ,shift):
    return encode(text,-shift)

def score_english(text):
    words = text.lower().split()
    score = 0
    for word in words:
        if word in common_words:
            score += 1
    return score

def brute_force(ciphertext):
    best_score = -1
    best_shift = 0
    best_text =   ""

    for shift in range(1,26):
        attempt = decode(ciphertext)    
        score = score_english(attempt)
        if score > best_score:
            best_score = score           
            best_shift = shift             
            best_text = attempt             

    return best_shift, best_text

if __name__ == "__main__":
    print("[1] Encode  [2] Decode  [3] Brute Force")
    choice = input("Choice: ").strip()

    if choice == "1":
        msg = input("Message: ")
        shift = int(input("Shift (1-25): "))
        print(f"Encoded: {encode(msg, shift)}")
    elif choice == "2":
        msg = input("Encoded message: ")
        shift = int(input("Shift used: "))
        print(f"Decoded: {decode(msg, shift)}")
    elif choice == "3":
        msg = input("Message to crack: ")
        shift, result = brute_force(msg)
        print(f"Best shift: {shift}")
        print(f"Cracked: {result}")  
        