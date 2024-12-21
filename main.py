import re

def password_strength(password):
    # Initialize strength score
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check for digits
    if re.search(r'\d', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    return score

def strength_suggestions(score):
    suggestions = []
    if score < 2:
        suggestions.append("Your password is very weak. Consider using at least 12 characters, including uppercase, lowercase, digits, and special characters.")
    elif score == 2:
        suggestions.append("Your password is weak. Try to add more characters and include a mix of uppercase, lowercase, digits, and special characters.")
    elif score == 3:
        suggestions.append("Your password is moderate. Consider adding more characters or special characters for better security.")
    elif score >= 4:
        suggestions.append("Your password is strong! Keep it secure.")

    return suggestions

def main():
    password = input("Enter your password: ")
    score = password_strength(password)
    suggestions = strength_suggestions(score)

    print(f"Password Strength Score: {score}/6")
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()
