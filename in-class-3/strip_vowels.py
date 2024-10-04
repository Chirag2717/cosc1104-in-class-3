# Authors: Chirag Khurana-100949693 and Saquib Ahmed Khan-100949697
# Date: 04 October 2024
# Description: This Python code removes all vowels from a given string and returns the modified string.

def strip_vowels(s):
 
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char

    return result

if __name__ == "__main__":
    # Here we are using a static value instead of user input
    static_input = "Scripting in Cloud Computing"
    result = strip_vowels(static_input)
    print(f"The string without vowels: {result}")