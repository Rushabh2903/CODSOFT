import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    # Prompt user for password length
    length = int(input("Enter the desired length of the password: "))

    # Generate password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
