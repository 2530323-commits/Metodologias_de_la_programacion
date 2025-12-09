
# Name: Santiago Joshue Chavez Rivera
# Matriculation: 2530323
# Group: IM 1-3
#
# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------
# A function in Python is a reusable block of code that performs a specific task.
# Parameters are variables declared in the function definition, while arguments
# are the actual values passed during a function call. Separating logic into
# reusable functions improves organization, readability, and reduces repetition.
# Returning values allows functions to be used flexibly instead of only printing.
# This document includes 6 problems demonstrating function design, validation,
# default parameters, naming conventions, and test cases.

# --------------------------------------------------
# PRINCIPLES AND BEST PRACTICES
# --------------------------------------------------
# - Prefer small, single-responsibility functions.
# - Avoid repeating logic: extract repeated code into functions.
# - Prefer pure functions when possible (same input -> same output).
# - Document every function: what it does, its parameters, and return value.
# - Use meaningful names such as calculate_bmi, apply_discount, etc.

# ==================================================
# =============== PROBLEM 1 ========================
# ==================================================
# Problem 1: Rectangle area and perimeter
# Description:
#   Program that defines two functions to calculate the area and perimeter
#   of a rectangle, validates user input, and prints the results.
#
# Inputs:
#   - width (float)
#   - height (float)
#
# Outputs:
#   - Area
#   - Perimeter
#
# Validations:
#   - width > 0
#   - height > 0
#
# Test cases:
#   1) Normal: width=5, height=3 → Area=15, Perimeter=16
#   2) Border: width=0.1, height=0.1 → valid small values
#   3) Error: width=-5 → "Error: invalid input"

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

# MAIN for Problem 1
width = 5
height = 3

if width > 0 and height > 0:
    print("Problem 1:")
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")


# ==================================================
# =============== PROBLEM 2 ========================
# ==================================================
# Problem 2: Grade classifier
# Description:
#   Determines grade category A–F based on score (0–100).
#
# Inputs:
#   - score (float)
#
# Outputs:
#   - Score and its category
#
# Validations:
#   - 0 <= score <= 100
#
# Test cases:
#   1) Normal: score=85 → B
#   2) Border: score=100 → A
#   3) Error: score=-10 → error message

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# MAIN for Problem 2
score = 85

if 0 <= score <= 100:
    print("\nProblem 2:")
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")


# ==================================================
# =============== PROBLEM 3 ========================
# ==================================================
# Problem 3: List statistics
# Description:
#   Receives a list of numbers and returns min, max and average.
#
# Inputs:
#   - numbers_list (list of floats)
#
# Outputs:
#   - Min, Max, Average
#
# Validations:
#   - List not empty
#   - All elements must be numbers
#
# Test cases:
#   1) Normal: [10,20,30] → min=10, max=30, avg=20
#   2) Border: [5] → min=5, max=5, avg=5
#   3) Error: [] → error

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }

# MAIN for Problem 3
numbers_text = "10,20,30"
try:
    numbers_list = [float(num) for num in numbers_text.split(",") if num.strip() != ""]
    if len(numbers_list) == 0:
        print("Error: invalid input")
    else:
        summary = summarize_numbers(numbers_list)
        print("\nProblem 3:")
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", summary["average"])
except:
    print("Error: invalid input")


# ==================================================
# =============== PROBLEM 4 ========================
# ==================================================
# Problem 4: Apply discount list
# Description:
#   Applies a discount rate to a list of prices.
#
# Inputs:
#   - prices_list (list of floats)
#   - discount_rate (float between 0 and 1)
#
# Outputs:
#   - Original list
#   - Discounted list
#
# Validations:
#   - prices_list not empty and all > 0
#   - 0 <= discount_rate <= 1
#
# Test cases:
#   1) Normal: [100, 200] with 0.1 → [90,180]
#   2) Border: rate=0 → same list
#   3) Error: rate=2 → invalid

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted

# MAIN for Problem 4
prices_text = "100,200,300"
discount_rate = 0.1

try:
    prices_list = [float(p) for p in prices_text.split(",") if p.strip() != ""]
    if any(p <= 0 for p in prices_list) or not (0 <= discount_rate <= 1):
        print("Error: invalid input")
    else:
        discounted = apply_discount(prices_list, discount_rate)
        print("\nProblem 4:")
        print("Original prices:", prices_list)
        print("Discounted prices:", discounted)
except:
    print("Error: invalid input")


# ==================================================
# =============== PROBLEM 5 ========================
# ==================================================
# Problem 5: Greeting function with default parameter
# Description:
#   Function greet(name, title="") returns a greeting like:
#   "Hello, Dr. Alice!"
#
# Inputs:
#   - name (string)
#   - title (optional string)
#
# Outputs:
#   - Greeting message
#
# Validations:
#   - name not empty
#
# Test cases:
#   1) Normal: name="Alice", title="Dr." → "Hello, Dr. Alice!"
#   2) Border: title empty → "Hello, Alice!"
#   3) Error: name empty → invalid

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if title != "":
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"

# MAIN for Problem 5
name = "Alice"
title = "Dr."

if name.strip() == "":
    print("Error: invalid input")
else:
    print("\nProblem 5:")
    print("Greeting:", greet(name, title=title))


# ==================================================
# =============== PROBLEM 6 ========================
# ==================================================
# Problem 6: Factorial function
# Description:
#   Computes n! using an iterative version.
#
# Inputs:
#   - n (int)
#
# Outputs:
#   - Factorial value
#
# Validations:
#   - n integer >= 0
#   - Optional: n <= 20
#
# Test cases:
#   1) Normal: n=5 → 120
#   2) Border: n=0 → 1
#   3) Error: n=-1 → invalid

def factorial(n):
    # Iterative implementation
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# MAIN for Problem 6
n = 6

if isinstance(n, int) and 0 <= n <= 20:
    print("\nProblem 6:")
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")


# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Functions improve structure, readability, and maintenance of programs.
# Using return values allows separating logic from presentation.
# Default parameters make functions more flexible for different contexts.
# Reusable functions help avoid duplicate logic and errors.
# Working on these 6 problems reinforced the difference between main logic
# and helper functions, and the importance of validations and naming.


# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python documentation - Defining Functions
# 2) Python Official Tutorial - More on Functions
# 3) RealPython - Best Practices for Functions in Python
# 4) W3Schools - Python Functions
# 5) Class notes on structured programming
# --------------------------------------------------
