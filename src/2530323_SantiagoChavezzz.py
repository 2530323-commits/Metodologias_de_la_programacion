

#Name: Santiago Joshue Chavez Rivera
#Matriculation: 2530323
#Group: IM 1-3


##EXECUTIVE SUMMARY

#This document explains the use of Python collections: lists (mutable), tuples (immutable),
#and dictionaries (key-value structures). Lists allow adding, removing, and modifying elements.
#Tuples store fixed, ordered data that must not change. Dictionaries associate keys with
#values, enabling fast lookups and structured storage. The problems in this file cover
#input design, output design, validations, and practical use of these collections for catalogs,
#records, calculations, and frequency processing.

##GOOD PRACTICES

#- Use lists when elements may be frequently added or removed.
#- Use tuples for data that should not change (coordinates, dates, fixed configs).
#- Use dictionaries for quick lookups by key (names, IDs, product codes).
#- Avoid modifying a list while iterating over it.
#- Use descriptive key names in dictionaries (e.g., "name", "age", "price").
#- Write readable code and clear messages for users.


##################################################
#                  PROBLEM 1                     #
##################################################
# Problem 1: Shopping list basics
# Description:
#   Work with a list of products (strings). The program must:
#   1) Create an initial list from a comma-separated string.
#   2) Add a new product.
#   3) Show total count.
#   4) Search for a specific product.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <count>
# - "Found item:" true|false
#
# Validations:
# - initial_items_text not empty
# - new_item not empty
# - search_item not empty
#
# Test cases:
# 1) Normal: "apple,banana", new_item="orange", search="banana"
# 2) Border: initial empty or spaces only
# 3) Error: item empty

initial_items_text = "apple, banana, orange"
new_item = "grape"
search_item = "orange"

# Validation
if not initial_items_text.strip() or not new_item.strip() or not search_item.strip():
    print("Error: invalid input")
else:
    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
    items_list.append(new_item)
    total_items = len(items_list)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", total_items)
    print("Found item:", str(is_in_list).lower())


##################################################
#                  PROBLEM 2                     #
##################################################
# Problem 2: Points and distances (tuples)
# Description:
#   Use tuples to represent two 2D points. Compute distance and midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" value
# - "Midpoint:" (mx, my)
#
# Validations:
# - All values must be convertible to float.
#
# Test cases:
# 1) Normal: (0,0) and (3,4)
# 2) Border: same point
# 3) Error: non-numeric input

x1, y1, x2, y2 = 0.0, 0.0, 3.0, 4.0

try:
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
except:
    print("Error: invalid input")
else:
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)


##################################################
#                  PROBLEM 3                     #
##################################################
# Problem 3: Product catalog (dictionary)
# Description:
#   Manage a small product catalog using a dict.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - Unit price, quantity, total OR error message
#
# Validations:
# - quantity > 0
# - product_name not empty
# - product must exist in dict
#
# Test cases:
# 1) Normal: apple, quantity 3
# 2) Border: quantity = 1
# 3) Error: product not found

product_prices = {
    "apple": 10.0,
    "banana": 8.0,
    "orange": 12.0
}

product_name = "apple"
quantity = 3

if not product_name.strip() or quantity <= 0:
    print("Error: invalid input")
elif product_name not in product_prices:
    print("Error: product not found")
else:
    unit_price = product_prices[product_name]
    total = unit_price * quantity

    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total)


##################################################
#                  PROBLEM 4                     #
##################################################
# Problem 4: Student grades (dictionary + list)
# Description:
#   Compute average of grades for a student.
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - Grades list, average, passed (true/false) OR error
#
# Validations:
# - student_name not empty
# - student exists
# - list not empty
#
# Test cases:
# 1) Normal: Alice
# 2) Border: grades = [70]
# 3) Error: student not found

grades = {
    "Alice": [90.0, 85.0, 88.0],
    "Bob": [70.0, 72.0],
    "Carol": [100.0, 95.0]
}

student_name = "Alice"

if not student_name.strip():
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    if len(grades[student_name]) == 0:
        print("Error: no grades available")
    else:
        average = sum(grades[student_name]) / len(grades[student_name])
        is_passed = average >= 70.0

        print("Grades:", grades[student_name])
        print("Average:", average)
        print("Passed:", str(is_passed).lower())


##################################################
#                  PROBLEM 5                     #
##################################################
# Problem 5: Word frequency counter
# Description:
#   Count word frequencies using list and dict.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Words list
# - Frequency dict
# - Most common word
#
# Validations:
# - sentence not empty
# - list not empty
#
# Test cases:
# 1) Normal: "This is a test this is"
# 2) Border: one word only
# 3) Error: empty string

sentence = "this is a test this is"

if not sentence.strip():
    print("Error: invalid input")
else:
    words_list = sentence.lower().split()
    freq_dict = {}

    for w in words_list:
        if w in freq_dict:
            freq_dict[w] += 1
        else:
            freq_dict[w] = 1

    most_common_word = None
    highest_count = 0

    for word, count in freq_dict.items():
        if count > highest_count:
            most_common_word = word
            highest_count = count

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)


##################################################
#                  PROBLEM 6                     #
##################################################
# Problem 6: Simple contact book (dictionary CRUD)
# Description:
#   Add, search, or delete contacts.
#
# Inputs:
# - action_text ("ADD", "SEARCH", "DELETE")
# - name (string)
# - phone (string if ADD)
#
# Outputs:
# - Operation results
#
# Validations:
# - action must be valid
# - name not empty
# - phone not empty for ADD
#
# Test cases:
# 1) Normal: ADD Alice 1234
# 2) Border: SEARCH unknown name
# 3) Error: invalid action

contacts = {
    "Alice": "1111",
    "Bob": "2222"
}

action_text = "ADD"
name = "Carol"
phone = "3333"

action_text = action_text.upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
elif not name.strip():
    print("Error: invalid input")
else:
    if action_text == "ADD":
        if not phone.strip():
            print("Error: invalid phone")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")



##CONCLUSIONS

# Collections in Python are essential tools for organizing data.
# Lists allow flexible insertion and removal of elements.
# Tuples ensure data remains unchanged, which is useful for coordinates.
# Dictionaries enable quick lookups by key and structured associations.
# Combining them (e.g., dict of lists) is a powerful pattern.
# These problems illustrate validation, processing, and output formatting.

##REFERENCES
# 1) Python Documentation - Built-in Types
# 2) Python.org Tutorials
# 3) "Automate the Boring Stuff with Python" - A. Sweigart
# 4) Real Python - Data Structures
# 5) Class notes and official course materials

