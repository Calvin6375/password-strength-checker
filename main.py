import re

def password_strength(password):
    # Initialize strength score
    score = 0
    feedback = [] 

    # Check the length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
