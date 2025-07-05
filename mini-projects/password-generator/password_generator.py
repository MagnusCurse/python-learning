# Import necessary modules
import random  # For random selection of characters
import string  # For string constants like ascii_letters, digits, punctuation


def generate_password(min_length, numbers=True, special_characters=True):
    """
        Generates a random password based on the specified criteria.
        :param min_length: Minimum length of the password
        :param numbers: Whether to include numbers in the password
        :param special_characters: Whether to include special characters in the password
        :return: Generated password as a string
    """
    letters = string.ascii_letters  # All uppercase and lowercase letters
    digits = string.digits          # All digit characters (0-9)
    special = string.punctuation    # All special characters (e.g., !@#$%)

    characters = letters  # Start with letters only
    if numbers:
        characters += digits  # Add digits if requested
    if special_characters:
        characters += special  # Add special characters if requested

    pwd = ""  # The password to be generated
    meets_criteria = False  # Flag to check if password meets all criteria
    has_number = False      # Flag to check if password has at least one number
    has_special = False     # Flag to check if password has at least one special character

    # Keep generating characters until the password meets all criteria and is long enough
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)  # Randomly select a character
        pwd += new_char  # Add the character to the password

        # Check if the new character is a digit
        if new_char in digits:
            has_number = True
        # Check if the new character is a special character
        elif new_char in special:
            has_special = True

        # Update criteria flags
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd  # Return the generated password


# Get user inputs
min_length = int(input("Enter the minimum length: "))  # Ask user for minimum password length
has_number = input("Do you want to have numbers? (y/n): ").lower() == 'y'  # Ask if numbers should be included
has_special = input("Do you want to have special characters? (y/n): ").lower() == 'y'  # Ask if special characters should be included

# Generate and display the password
pwd = generate_password(min_length, has_number, has_special)  # Generate password with user preferences
print("Generated password is:", pwd)  # Print the generated password
