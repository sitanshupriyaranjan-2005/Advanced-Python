def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("After removing duplicates:", remove_duplicates(numbers))ø
