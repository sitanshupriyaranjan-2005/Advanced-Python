def largest(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number:", largest(numbers))
