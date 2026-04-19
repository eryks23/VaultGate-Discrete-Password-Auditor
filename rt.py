import string

def check_password_strength(password):

    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters)")
        
    password_chars = set(password)
    
    has_lower = not password_chars.isdisjoint(string.ascii_lowercase)
    has_upper = not password_chars.isdisjoint(string.ascii_uppercase)
    has_digits = not password_chars.isdisjoint(string.digits)
    has_symbols = not password_chars.isdisjoint(string.punctuation)
    
    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")
        
    if has_upper:
        score += 1
    else: 
        feedback.append("Add uppercase letters")
        
    if has_digits:
        score += 1
    else:
        feedback.append("Add numbers")
    
    if has_symbols: score += 1
    else: feedback.append("Add special characters")
    
    if score >= 5:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback
    
user_input = input("Enter your password to check: ")
strength, suggestions = check_password_strength(user_input)

print(f"\nPassword Strength: {strength}")

if suggestions:
    print("Suggestions to improve: ")
    
    for tip in suggestions:
        print(f"- {tip}")
