import re

def validate_name(name):
    if len(name) < 2:
        return False
    if re.search(r'[<>]', name):
        return False
    return True

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def main():
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    if not validate_name(name):
        print("Invalid name. Name should be at least 2 characters long and not contain '<' or '>'.")
        return

    if not validate_email(email):
        print("Invalid email format.")
        return

    print("Registration successful!")

if __name__ == "__main__":
    main()