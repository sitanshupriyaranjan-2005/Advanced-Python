def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter how many numbers: "))
fibonacci(num)
