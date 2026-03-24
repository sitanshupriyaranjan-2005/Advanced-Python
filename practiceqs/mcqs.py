'''x = [1,2,3]
print(x * 2)'''
#o/p [1, 2, 3, 1, 2, 3]

#print(bool(""))
#o/p False

# Which is mutable? o/p  list
#print(10 == 10.0) o/p True
'''a = [1,2,3]
b = a
b.append(4)
print(a) '''
#o/p [1, 2, 3, 4]

'''def func(x=[]):
    x.append(1)
    return x
print(func())
print(func()) '''
'''o/p:
[1]
[1, 1]'''

'''for i in range(5):
    if i == 3:
        break
    print(i)
o/p: 
0
1   
2'''

"""try:
    print(10/0)
except:
    print("Error")
finally:
    print("Done")"""
#o/p:
#Error  
#Done

"""# Take input string
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():   # check only letters
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
o/p:
Enter a string: sitanshu
Vowels: 3
Consonants: 5"""

'''# Open and read file
filename = input("Enter file name: ")

with open(filename, 'r') as file:
    content = file.read()

# Count lines
lines = content.split('\n')
line_count = len(lines)

# Count words
words = content.split()
word_count = len(words)

# Count characters
char_count = len(content)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)'''
'''o/p:
Enter file name: netaji.txt
Lines: 1
Words: 0
Characters: 0'''

"""class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Create object
acc = BankAccount()

# Example operations
acc.deposit(1000)
acc.withdraw(500)
acc.check_balance()
o/p:
Deposited: 1000
Withdrawn: 500
Current Balance: 500"""

"""# Accept input
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Remove duplicates
unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

# Sort without using sort() (Bubble Sort)
n = len(unique_nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if unique_nums[j] > unique_nums[j + 1]:
            # swap
            unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]

print("Sorted list without duplicates:", unique_nums)

Enter numbers separated by space: 5 2 3 2 1 5
Sorted list without duplicates: [1, 2, 3, 5]"""

"""# Input list
nums = list(map(int, input("Enter numbers: ").split()))

# Filter even numbers and square them
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print("Squared even numbers:", result)

o/p:
Enter numbers: 1 2 3 4 5 6
Squared even numbers: [4, 16, 36]"""


"""# File name to store user data
filename = "users.txt"

# Function to register new user
def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open(filename, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful!")

# Function to login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(filename, "r") as file:
        users = file.readlines()

    for user in users:
        u, p = user.strip().split(",")
        if u == username and p == password:
            print("Login successful!")
            return

    print("Invalid username or password!")

# Main menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
        
o/p
1. Register
2. Login
3. Exit
Enter choice: 1
Enter new username: sitanshu
Enter new password: sita@2005@
Registration successful!

1. Register
2. Login
3. Exit"""

"""# Create custom exception
class InvalidAgeError(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above!")
    else:
        print("Access granted!")

# Main
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid number!")

o/p:Enter your age: 17
Error: Age must be 18 or above!"""




"""import tkinter as tk

# Function to handle button click
def submit_name():
    name = entry.get()
    result_label.config(text="Hello, " + name)

# Create window
root = tk.Tk()
root.title("Name Form")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
submit_btn = tk.Button(root, text="Submit", command=submit_name)
submit_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run app
root.mainloop()"""

"""import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sita@202428",
    database="gietu"   # make sure this DB exists
)

cursor = conn.cursor()

# Create table
cursor.execute("""
#CREATE TABLE IF NOT EXISTS Student (
"""
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)"""
""")

# Insert records
cursor.execute("INSERT INTO Student VALUES (1, 'Rahul', 20)")
cursor.execute("INSERT INTO Student VALUES (2, 'Anita', 22)")
cursor.execute("INSERT INTO Student VALUES (3, 'Ravi', 19)")

conn.commit()

# Fetch records
cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# Close connection
conn.close()

o/pStudent Records:
(1, 'Rahul', 20)
(2, 'Anita', 22)
(3, 'Ravi', 19)"""


filename = "students.txt"

# Add student
def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    with open(filename, "a") as f:
        f.write(sid + "," + name + "," + age + "\n")

    print("✅ Student added successfully!")

# View students
def view_students():
    try:
        with open(filename, "r") as f:
            data = f.readlines()

        if not data:
            print("No records found!")
            return

        print("\n--- Student List ---")
        for line in data:
            sid, name, age = line.strip().split(",")
            print(f"ID: {sid}, Name: {name}, Age: {age}")

    except FileNotFoundError:
        print("No file found!")

# Delete student
def delete_student():
    sid = input("Enter ID to delete: ")

    try:
        with open(filename, "r") as f:
            data = f.readlines()

        new_data = []
        found = False

        for line in data:
            if line.split(",")[0] != sid:
                new_data.append(line)
            else:
                found = True

        with open(filename, "w") as f:
            f.writelines(new_data)

        if found:
            print("🗑️ Student deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("No file found!")

# Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")