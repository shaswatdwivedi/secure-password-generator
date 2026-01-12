import random
import string


def generate_password(length, use_symbols=True, use_numbers=True):
    """
    Generates a random password based on user preferences.
    """
    # 1. Start with basic letters (a-z, A-Z)
    characters = string.ascii_letters

    # 2. Add numbers as per user requirement
    if use_numbers:
        characters += string.digits  # Adds '0123456789'

    # 3. Add symbols if requested (like !,@,#,$,%.^.&)
    if use_symbols:
        characters += string.punctuation  # Adds '!@#$...'

    # 4. Generate the password
    # We pick a random character from our list 'length' times
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("--- Secure Password Generator ---")

    # Get user inputs

    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print("Error: Please enter a number.")
        return

    include_syms = input("Include symbols? (y/n): ").lower() == 'y'
    include_nums = input("Include numbers? (y/n): ").lower() == 'y'

    # Call the function
    new_password = generate_password(length, include_syms, include_nums)

    print("\n-----------------------------")
    print(f"Your Secure Password: {new_password}")
    print("-----------------------------")

    # TO automatically Save a file with password in it
    save = input("Do you want to save this to a file? (y/n): ")
    if save.lower() == 'y':
        with open("my_passwords.txt", "a") as f:
            f.write(f"{new_password}\n")
        print("Password saved to my_passwords.txt!")


# This tells Python to run the main function if this file is executed
if __name__ == "__main__":
    main()