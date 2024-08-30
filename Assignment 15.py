def is_palindrome(s):

    cleaned_string = ''.join(s.split()).lower()

    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("Hello"))  # Output: False