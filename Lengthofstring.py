def string_length(s):
    count = 0
    for ch in s:
        count += 1
    return count

text = input("Enter a string: ")
print("Length of string:", string_length(text))
