import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
