import random
import string

def gen_passwd():
    length = int(input("Enter the desired length: ").strip())
    include_uppercase = input("Include uppercase? (Y/N): ").strip().upper()
    include_lowercase = input("Include lowercase? (Y/N): ").strip().upper()
    include_special = input("Include special characters? (Y/N): ").strip().upper()
    include_digit = input("Include digits? (Y/N): ").strip().upper()

    if length < 4:
        print("Password must have a character count higher than four.")
        return

    # Build character pools
    lower = string.ascii_lowercase if include_lowercase == 'Y' else ""
    upper = string.ascii_uppercase if include_uppercase == 'Y' else ""
    special = string.punctuation if include_special == 'Y' else ""
    digits = string.digits if include_digit == 'Y' else ""

    all_char = lower + upper + special + digits

    if not all_char:
        print("You must select at least one character type.")
        return

    # Ensure at least one character from each selected type
    required = []
    if upper:
        required.append(random.choice(upper))
    if lower:
        required.append(random.choice(lower))
    if special:
        required.append(random.choice(special))
    if digits:
        required.append(random.choice(digits))

    remaining = length - len(required)
    password = required + [random.choice(all_char) for _ in range(remaining)]
    random.shuffle(password)

    return ''.join(password)

# Generate and display password
password = gen_passwd()
if password:
    print("Generated Password:", password)

gen_passwd()

