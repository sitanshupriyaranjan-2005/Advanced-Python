#Find the largest element in a list.
# lst = [10, 20, 5, 40]
# print(max(lst))

#Check if a number is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#Reverse a string (without slicing).
# s = "hello"
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)

#Count vowels in a string.
# s = "hello world"
# count = 0
# for ch in s:
#     if ch in 'aeiouAEIOU':    
#         count += 1
# print("Number of vowels:", count)

#Find the sum of digits of a number.
# num = 12345
# total = 0 
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10    
# print("Sum of digits:", total)

#Check if a string is a palindrome.
# s = "madam"
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Print Fibonacci series up to N terms.
# n = 10
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

#Swap two variables without a third variable.
# a = 5
# b = 10
# a = a + b
# b = a - b
# a = a - b
# print("a =", a, "b =", b)

#Count words in a sentence.
# sentence = "Hello world, welcome to Python programming."
# words = sentence.split()
# print("Number of words:", len(words))

#Find minimum and maximum in a list
# lst = [10, 20, 5, 40]
# print("Minimum:", min(lst))
# print("Maximum:", max(lst))

#Find the second largest number in a list.
# lst = [10, 20, 5, 40]
# lst.sort()
# print("Second largest:", lst[-2])

#Remove duplicates from a list (without set).
# lst = [1, 2, 3, 2, 4, 1]
# unique_lst = []
# for item in lst:
#     if item not in unique_lst:
#         unique_lst.append(item)
# print(unique_lst)

#Count frequency of elements in a list.
# lst = [1, 2, 3, 2, 4, 1]
# freq = {}
# for item in lst:
#     freq[item] = freq.get(item, 0) + 1
# print(freq)

#Merge two sorted lists.
# lst1 = [1, 3, 5]
# lst2 = [2, 4, 6]
# print(sorted(lst1 + lst2))

#Find the intersection of two lists.
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# intersection = list(set(list1) & set(list2))

# print(intersection)

#Rotate a list by k positions.
# lst = [1, 2, 3, 4, 5]
# k = 2
# rotated_lst = lst[k:] + lst[:k]
# print(rotated_lst)

#Check if two strings are anagrams.
# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):  
#     print("Anagrams")
# else:
#     print("Not anagrams")

#Find the first non-repeating character.
# s = "swiss"
# char_count = {}
# for ch in s:
#     char_count[ch] = char_count.get(ch, 0) + 1
# for ch in s:
#     if char_count[ch] == 1:
#         print("First non-repeating character:", ch)
#         break
# else:
#     print("No non-repeating character found")

#Flatten a nested list.
# nested_list = [[1, 2], [3, 4], [5]]
# flat_list = [item for sublist in nested_list for item in sublist]
# print(flat_list)

#Find all pairs with a given sum.
# lst = [1, 2, 3, 4, 5]
# target_sum = 5
# pairs = []
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] + lst[j] == target_sum:
#             pairs.append((lst[i], lst[j]))
# print(pairs)

#Print a right triangle pattern.
# n = 5
# for i in range(1, n + 1):
#     print("*" * i)


#Print a pyramid pattern.
# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

#Print all prime numbers in a range.
# start = 10
# end = 50
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")

#Check if a number is Armstrong.
num = 153
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
