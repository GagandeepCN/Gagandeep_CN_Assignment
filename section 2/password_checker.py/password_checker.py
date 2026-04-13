import re

def check_password(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Lowercase check
    if re.search("[a-z]", password):
        strength += 1

    # Uppercase check
    if re.search("[A-Z]", password):
        strength += 1

    # Number check
    if re.search("[0-9]", password):
        strength += 1

    # Special character check
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    # Result
    if strength <= 2:
        return "Weak ❌"
    elif strength == 3 or strength == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

def main():
    print("==== Password Strength Checker ====")
    password = input("Enter your password: ")
    result = check_password(password)
    print("Password Strength:", result)

if __name__ == "__main__":
    main()
