# Authors: Chirag Khurana-100949693 and Saquib Ahmed Khan-100949697
# Date: 04 October 2024
# Description: This Python code converts a given string to lowercase, removing spaces, punctuation, and special characters, except underscores.

def force_strict_case(s):
    
    result = ""
    for char in s:
        # Here we are only keeping alphanumeric characters and underscores
        if char.isalnum() or char == '_':  
            # Convert to lowercase
            result += char.lower()  

    return result

if __name__ == "__main__":
    # Here we are using a static value instead of user input
    static_input = "Python_Durham_College!"
    result = force_strict_case(static_input)
    print(f"Formatted string: {result}")