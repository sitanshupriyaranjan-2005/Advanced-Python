def is_palindrome(s):
    return s == s[::-1]
word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
