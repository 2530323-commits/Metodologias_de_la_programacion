
# Name: Santiago Joshue Chavez Rivera
# Student ID: 2530323
# Group:IM 1-3
#

# --------------------------------------------------
# 2. EXECUTIVE SUMMARY
# --------------------------------------------------
# In this document I explain the concepts and correct usage of Python loops,
# specifically for and while. A for loop is typically used when the number of
# iterations is known, while a while loop is used when repetition depends on a
# condition. I also describe counters and accumulators as fundamental tools
# inside loops to keep track of repetitions or cumulative totals. Additionally,
# I highlight the importance of defining clear stopping conditions to avoid
# infinite loops. This file includes six problems with inputs, outputs,
# validations, and test cases demonstrating different loop scenarios such as
# ranges, sentinel-controlled loops, attempt limits, and menus.

# --------------------------------------------------
# 3. PRINCIPLES AND BEST PRACTICES
# --------------------------------------------------
# - Use for loops when the number of iterations is known.
# - Use while loops when the number of iterations depends on a condition.
# - Initialize counters and accumulators before entering the loop.
# - Always update while-loop control variables to prevent infinite loops.
# - Keep loop bodies simple and readable; extract complex logic into functions.

# ==================================================
# 4. PROBLEM 1: SUM OF RANGE WITH FOR
# ==================================================
# Description:
#   Computes the sum of numbers from 1 to n and also the sum of even numbers
#   in the same range using a for loop.
# Inputs:
#   - n (int)
# Outputs:
#   - "Sum 1..n:" total_sum
#   - "Even sum 1..n:" even_sum
# Validations:
#   - n must be convertible to int
#   - n >= 1
# Test cases:
#   1) Normal: n=10 → sum=55, even_sum=30
#   2) Border: n=1 → sum=1, even_sum=0
#   3) Error: n=0 → "Error: invalid input"

# --- CODE ---
try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except:
    print("Error: invalid input")

# ==================================================
# 5. PROBLEM 2: MULTIPLICATION TABLE WITH FOR
# ==================================================
# Description:
#   Prints the multiplication table of a base number from 1 to m.
# Inputs:
#   - base (int)
#   - m (int)
# Outputs:
#   - Lines formatted as: "base x i = result"
# Validations:
#   - base and m convertible to int
#   - m >= 1
# Test cases:
#   1) Normal: base=5, m=4
#   2) Border: m=1
#   3) Error: m=0 → "Error: invalid input"

# --- CODE ---
try:
    base = int(input("Enter base: "))
    m = int(input("Enter limit: "))
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except:
    print("Error: invalid input")

# ==================================================
# 6. PROBLEM 3: AVERAGE WITH WHILE + SENTINEL
# ==================================================
# Description:
#   Reads numbers until sentinel -1 is entered. Computes count and average.
# Inputs:
#   - number (float repeatedly)
# Outputs:
#   - "Count:" value
#   - "Average:" value
# Validations:
#   - each number must be float-convertible
# Test cases:
#   1) Normal: inputs 5,10, -1 → count=2, avg=7.5
#   2) Border: input -1 immediately → "Error: no data"
#   3) Error: invalid float → error message but continues

# --- CODE ---
sentinel_value = -1
count = 0
sum_values = 0.0

while True:
    user_input = input("Enter number (-1 to stop): ")
    try:
        number = float(user_input)
    except:
        print("Error: invalid input")
        continue

    if number == sentinel_value:
        break

    count += 1
    sum_values += number

if count == 0:
    print("Error: no data")
else:
    print("Count:", count)
    print("Average:", sum_values / count)

# ==================================================
# 7. PROBLEM 4: PASSWORD ATTEMPTS WITH WHILE
# ==================================================
# Description:
#   User must guess the correct password within MAX_ATTEMPTS tries.
# Inputs:
#   - user_password (string)
# Outputs:
#   - "Login success" or "Account locked"
# Validations:
#   - attempts counted correctly
# Test cases:
#   1) Normal: correct on 2nd try
#   2) Border: correct on last try
#   3) Error: all attempts wrong → lock

# --- CODE ---
CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    pwd = input("Enter password: ")
    if pwd == CORRECT_PASSWORD:
        print("Login success")
        break
    attempts += 1
else:
    print("Account locked")

# ==================================================
# 8. PROBLEM 5: SIMPLE MENU WITH WHILE
# ==================================================
# Description:
#   Shows a menu repeatedly until user selects 0.
# Inputs:
#   - option (int)
# Outputs:
#   - greeting, counter value, increment message, exit message
# Validations:
#   - option must be 0,1,2,3
# Test cases:
#   1) Normal: choose 1,2,3,0
#   2) Border: exit immediately with 0
#   3) Error: invalid option → error message

# --- CODE ---
counter = 0
while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Option: ")
    try:
        option = int(option_input)
    except:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")

# ==================================================
# 9. PROBLEM 6: PATTERN PRINTING WITH NESTED LOOPS
# ==================================================
# Description:
#   Prints a right‑triangle pattern of asterisks.
# Inputs:
#   - n (int)
# Outputs:
#   - pattern lines
# Validations:
#   - n >= 1
# Test cases:
#   1) Normal: n=4
#   2) Border: n=1
#   3) Error: n=0 → "Error: invalid input"

# --- CODE ---
try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            print("*" * i)
except:
    print("Error: invalid input")

# --------------------------------------------------
# 10. CONCLUSIONS
# --------------------------------------------------
# In this assignment I explored the differences between for and while loops and
# saw how each is useful in different scenarios. Counters and accumulators were
# essential for controlling repetition and computing results. I learned that
# while loops require extra caution to avoid infinite cycles by updating control
# variables properly. Menu systems and password attempts demonstrated practical
# real‑world applications of loop logic. Nested loops allowed me to generate
# structured patterns, reinforcing the concept of iteration within iteration.

# --------------------------------------------------
# 11. REFERENCES
# --------------------------------------------------
# 1) Python documentation - for and while statements
# 2) Python official tutorial - Control Flow Tools
# 3) Online Python loop pattern resources
# 4) Programming Logic & Algorithms textbooks
# 5) Course lecture notes on loop structures
