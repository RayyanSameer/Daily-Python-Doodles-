#Cryptography logic shows up in security tooling and auth systems. The brute-force cracker introduces scoring heuristics — "score each option, pick the best one" is exactly how AI ranking and classification systems work at a basic level. This pattern shows up everywhere in AI engineering.

def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char        # 
    return result

if __name__ == "__main__":
    print(encode("Rayyan Sameer", 3))   
    print(encode("Khoor Zruog", -3))  # Hello World