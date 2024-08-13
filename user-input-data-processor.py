# Task 1: Input Length Validator

# Check if names are at minimum 2 character long
def validate_name_length(first_name, last_name):
    # Check first name
    if len(first_name) < 2:
        print("Error: Name must be at least 2 characters long.")
    # Check last name
    if len(last_name) < 2:
        print("Error: Name must be at least 2 characters long.")
    # If names are valid, print message
    if len(first_name) >= 2 and len(last_name) >= 2:
        print("Thank you! Both names are valid.")

# Ask for user input
def get_user_input():
    # Enter first name
    first_name = input("Please enter your first name: ")
    # Enter last name
    last_name = input("Please enter your last name: ")
    validate_name_length(first_name, last_name)

# Run program
get_user_input()