
# Authors: Chirag Khurana-100949693 and Saquib Ahmed Khan-100949697
# Date: 04 October 2024
# Description: This Python code checks if a given string is a palindrome, ignoring punctuation and spaces.

def is_palindrome(s):
    # Here we are removing spaces, punctuation, and convert to lowercase manually
    cleaned_s = ""
    for char in s:
        if char.isalnum():  # Only include alphanumeric characters
            cleaned_s += char.lower()

    # Here we are Checking if the cleaned string is a palindrome
    start = 0
    end = len(cleaned_s) - 1

    while start < end:
        if cleaned_s[start] != cleaned_s[end]:
            return False
        start += 1
        end -= 1

    return True

if __name__ == "__main__":
    # Here we are using a static value instead of user input
    static_input = "naman"
    result = is_palindrome(static_input)
    print(f"Is the string '{static_input}' a palindrome? {result}")