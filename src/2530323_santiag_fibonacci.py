
# Name: Santiago Joshue Chavez Rivera
# Matriculation: 2530323
# Group: IM 1-3
#
# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------
# The Fibonacci series is a sequence of numbers where each term is the
# sum of the previous two, starting with 0 and 1. Calculating the series
# up to n terms means generating the first n values of this sequence.
# This program reads an integer n, validates it, and prints the first
# n Fibonacci terms using a simple loop structure.

# --------------------------------------------------
# PROBLEM DOCUMENTATION
# --------------------------------------------------
# Problem: Fibonacci series generator
#
# Description:
# Program that reads an integer n and prints the first n terms of the
# Fibonacci series starting at 0 and 1.
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - "Fibonacci series:" followed by the n terms separated by spaces
#
# Validations:
# - n must be an integer
# - n must be >= 1
# - Optional maximum limit: n <= 50 to avoid extremely large sequences
#
# Test cases:
# 1) Normal: n = 7 → expected: 0 1 1 2 3 5 8
# 2) Border: n = 1 → expected: 0
# 3) Error: n = -3 or n = "abc" → expected: "Error: invalid input"
#
# Optional:
# Diagram of flow (text description):
# - Start → read n → validate → if invalid: print error → stop.
# - If valid: use loop to generate Fibonacci terms → print series → end.
# --------------------------------------------------


# --------------------------------------------------
# FIBONACCI PROGRAM (MAIN CODE)
# --------------------------------------------------

# Read user input
user_input = input("Number of terms: ")

# Validate input
try:
    terms_count = int(user_input)
    
    if terms_count < 1 or terms_count > 50:
        print("Error: invalid input")
        exit()

except ValueError:
    print("Error: invalid input")
    exit()

# Generate Fibonacci series
print("Fibonacci series:")

# Case n = 1
if terms_count == 1:
    print("0")
    exit()

# General case n >= 2
first_term = 0
second_term = 1

print(first_term, second_term, end=" ")

count = 2

while count < terms_count:
    next_term = first_term + second_term
    print(next_term, end=" ")
    first_term = second_term
    second_term = next_term
    count += 1

print()  # Line break at the end


# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Using a loop simplified the creation of the Fibonacci sequence, since
# each term depends on the previous two values. Handling special cases
# such as n = 1 or n = 2 ensures the program behaves correctly with
# minimal inputs. Validating user input prevents errors and unexpected
# behavior. This logic could be adapted for more complex programs,
# including mathematical tools or numerical analysis scripts.

# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python Documentation – for and while loops.
# 2) TutorialsPoint – Python Fibonacci Examples.
# 3) Official class notes on introductory Python programming.
# --------------------------------------------------
