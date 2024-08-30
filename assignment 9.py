#input
char_input = input("Enter a single character: ")

if len(char_input) != 1 or not char_input.isalpha():
    if len(char_input) != 1:
        print("Error: Please enter only one character")
    else:
        print("Error: THe input is not a letter")
#Processing
else:
    char = char_input.lower()
    print("The character is a vowel")
    if char not in 'aeiou':
        print("the character is consonant")
