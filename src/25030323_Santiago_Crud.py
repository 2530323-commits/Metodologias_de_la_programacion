
# Name: Santiago Joshue Chavez Rivera
# Matriculation: 2030323    
# Group: IM1-3
#
# Problem: In-memory CRUD manager with functions
#
# --------------------------------------------------
# Executive summary (5-8 lines):
# A CRUD application performs Create, Read, Update and Delete operations on data.
# This program implements an in-memory CRUD for simple inventory items (id, name, price, quantity).
# I chose a dictionary mapping item_id -> item_dict because lookups, inserts and deletions by id are O(1)
# and it naturally enforces uniqueness of the id key. Using functions separates responsibilities:
# each CRUD operation is its own function, making the code easier to test, maintain and reuse.
# The program includes a text menu with options to create, read, update, delete, list items and exit.
#
# --------------------------------------------------
# Description:
# Program that implements a CRUD (Create, Read, Update, Delete) manager using functions,
# with validation and a menu-driven interface. Data is stored in a Python dict in memory.
#
# Inputs:
# - Menu option (int)
# - For CREATE/UPDATE: item_id (string), name (string), price (float), quantity (int)
# - For READ/DELETE: item_id (string)
#
# Outputs:
# - Informational messages: "Item created", "Item updated", "Item deleted", "Item not found",
#   "Error: invalid input", "Items list:"
#
# Validations:
# - Menu option must be valid (0..5)
# - item_id must not be empty after strip()
# - price must be convertible to float and >= 0.0
# - quantity must be convertible to int and >= 0
# - Disallow creating an item with an id already in use
# - For READ/UPDATE/DELETE, if the id does not exist, show "Item not found"
#
# Test cases (described; also provided as an automated demo function):
# 1) Normal: Create item "A1" -> read "A1" -> update "A1" -> delete "A1" → expected messages and final state empty.
# 2) Border: Create item with quantity = 0 and price = 0.0 (valid minimal numeric values).
# 3) Error: Attempt to create with empty id, invalid price ("abc") or invalid menu option -> "Error: invalid input".
#
# Filename convention: matricula_ApellidoNombre.py  (example: 1030034_CarlosTovar.py)
#
# Data structure choice:
# - Option chosen: A (dict where key = item_id, value = dict with fields "name", "price", "quantity")
# - Reason: fast lookup and natural uniqueness enforcement for item_id.
#
# --------------------------------------------------
# References:
# 1) https://docs.python.org/3/tutorial/datastructures.html  - Python data structures (dict, list)
# 2) https://docs.python.org/3/tutorial/controlflow.html   - Defining functions and control flow
# 3) https://realpython.com/python-dicts/                 - Practical dict usage and examples
#
# --------------------------------------------------

# -------------------------
# Constants (UPPER_SNAKE_CASE)
# -------------------------
EXIT_OPTION = 0
CREATE_OPTION = 1
READ_OPTION = 2
UPDATE_OPTION = 3
DELETE_OPTION = 4
LIST_OPTION = 5

VALID_OPTIONS = {EXIT_OPTION, CREATE_OPTION, READ_OPTION, UPDATE_OPTION, DELETE_OPTION, LIST_OPTION}

# -------------------------
# CRUD functions
# -------------------------
def create_item(items_dict, item_id, name, price, quantity):
    """
    Create a new item in items_dict.
    Returns:
      True if created successfully,
      False if item_id already exists.
    Preconditions/validation should be performed before calling.
    """
    if item_id in items_dict:
        return False
    items_dict[item_id] = {"name": name, "price": price, "quantity": quantity}
    return True

def read_item(items_dict, item_id):
    """
    Return the item dict if found, otherwise None.
    """
    return items_dict.get(item_id)

def update_item(items_dict, item_id, new_name=None, new_price=None, new_quantity=None):
    """
    Update an existing item.
    Only non-None fields are updated.
    Returns:
      True if updated,
      False if item not found.
    """
    item = items_dict.get(item_id)
    if item is None:
        return False
    if new_name is not None:
        item["name"] = new_name
    if new_price is not None:
        item["price"] = new_price
    if new_quantity is not None:
        item["quantity"] = new_quantity
    return True

def delete_item(items_dict, item_id):
    """
    Delete item by item_id.
    Returns True if deleted, False if not found.
    """
    if item_id in items_dict:
        del items_dict[item_id]
        return True
    return False

def list_items(items_dict):
    """
    Return a list of item representations (tuples) for display or testing.
    Each item represented as (id, name, price, quantity).
    """
    return [(item_id, v["name"], v["price"], v["quantity"]) for item_id, v in items_dict.items()]

# -------------------------
# Validation helpers
# -------------------------
def validate_item_id(raw_id):
    """
    Validate that item_id is not empty after stripping.
    Returns the stripped id or None if invalid.
    """
    if raw_id is None:
        return None
    item_id = str(raw_id).strip()
    if item_id == "":
        return None
    return item_id

def validate_name(raw_name):
    if raw_name is None:
        return None
    name = str(raw_name).strip()
    if name == "":
        return None
    return name

def validate_price(raw_price):
    """
    Try to convert raw_price to float and ensure >= 0.0.
    Returns float or None.
    """
    try:
        price = float(raw_price)
    except (TypeError, ValueError):
        return None
    if price < 0.0:
        return None
    return price

def validate_quantity(raw_quantity):
    """
    Try to convert raw_quantity to int and ensure >= 0.
    Returns int or None.
    """
    try:
        quantity = int(raw_quantity)
    except (TypeError, ValueError):
        return None
    if quantity < 0:
        return None
    return quantity

# -------------------------
# User interaction helpers
# -------------------------
def print_menu():
    print("\n--- Inventory CRUD Menu ---")
    print(f"{CREATE_OPTION}) Create item")
    print(f"{READ_OPTION}) Read item by id")
    print(f"{UPDATE_OPTION}) Update item by id")
    print(f"{DELETE_OPTION}) Delete item by id")
    print(f"{LIST_OPTION}) List all items")
    print(f"{EXIT_OPTION}) Exit")

def prompt_input(prompt_text):
    try:
        return input(prompt_text)
    except EOFError:
        # If input stream closes, act like exit
        return ""

# -------------------------
# Automated/demo test cases
# -------------------------
def demo_test_cases():
    """
    Runs the 3 demo test cases described in the header:
    1) Normal flow: create -> read -> update -> delete
    2) Border: create with price=0.0 and quantity=0
    3) Error: attempt invalid operations
    Prints results to the console.
    """
    print("\n--- Running demo test cases ---")
    demo_items = {}

    # Test 1: Normal
    print("\nTest 1: Normal case")
    ok = create_item(demo_items, "A1", "Widget", 9.99, 10)
    print("Create A1:", "Item created" if ok else "Item not created")
    item = read_item(demo_items, "A1")
    print("Read A1:", item if item else "Item not found")
    upd = update_item(demo_items, "A1", new_name="Widget Pro", new_price=12.5, new_quantity=8)
    print("Update A1:", "Item updated" if upd else "Item not found")
    print("Read A1 after update:", read_item(demo_items, "A1"))
    deleted = delete_item(demo_items, "A1")
    print("Delete A1:", "Item deleted" if deleted else "Item not found")
    print("Final items:", list_items(demo_items))

    # Test 2: Border values
    print("\nTest 2: Border case (price=0.0, quantity=0)")
    ok2 = create_item(demo_items, "B2", "Free Sample", 0.0, 0)
    print("Create B2:", "Item created" if ok2 else "Item not created")
    print("B2:", read_item(demo_items, "B2"))
    # cleanup
    delete_item(demo_items, "B2")

    # Test 3: Error handling
    print("\nTest 3: Error cases")
    # empty id
    invalid_id = validate_item_id("   ")
    print("Validate empty id ->", "Invalid" if invalid_id is None else "Valid")
    # invalid price
    invalid_price = validate_price("abc")
    print("Validate price 'abc' ->", "Invalid" if invalid_price is None else "Valid")
    # duplicate id create
    create_item(demo_items, "C3", "Sample C", 1.0, 1)
    dup = create_item(demo_items, "C3", "Sample C2", 2.0, 2)
    print("Create duplicate C3 ->", "Item created" if dup else "Item already exists")
    # invalid update (non-existent)
    upd_non = update_item(demo_items, "NOID", new_name="X")
    print("Update non-existent ->", "Item updated" if upd_non else "Item not found")
    # cleanup
    delete_item(demo_items, "C3")

    print("\n--- Demo test cases complete ---\n")

# -------------------------
# Main loop
# -------------------------
def main():
    items = {}  # main data structure: dict item_id -> {"name","price","quantity"}

    # Optionally run demo test cases first to satisfy the '3 cases of test' requirement
    # Uncomment the next line to run demos automatically at start, or keep as a visible demo call.
    demo_test_cases()

    while True:
        print_menu()
        raw_option = prompt_input("Enter option: ").strip()
        if raw_option == "":
            print("Error: invalid input")
            continue
        # Validate menu option as integer
        try:
            option = int(raw_option)
        except ValueError:
            print("Error: invalid input")
            continue

        if option not in VALID_OPTIONS:
            print("Error: invalid input")
            continue

        if option == EXIT_OPTION:
            print("Exiting program.")
            break

        if option == CREATE_OPTION:
            raw_id = prompt_input("Enter item id: ")
            item_id = validate_item_id(raw_id)
            if item_id is None:
                print("Error: invalid input")
                continue
            if item_id in items:
                print("Error: invalid input")
                # also show more specific message
                print("Item already exists")
                continue
            raw_name = prompt_input("Enter name: ")
            name = validate_name(raw_name)
            if name is None:
                print("Error: invalid input")
                continue
            raw_price = prompt_input("Enter price: ")
            price = validate_price(raw_price)
            if price is None:
                print("Error: invalid input")
                continue
            raw_quantity = prompt_input("Enter quantity: ")
            quantity = validate_quantity(raw_quantity)
            if quantity is None:
                print("Error: invalid input")
                continue
            created = create_item(items, item_id, name, price, quantity)
            if created:
                print("Item created")
            else:
                print("Item already exists")

        elif option == READ_OPTION:
            raw_id = prompt_input("Enter item id to read: ")
            item_id = validate_item_id(raw_id)
            if item_id is None:
                print("Error: invalid input")
                continue
            item = read_item(items, item_id)
            if item is None:
                print("Item not found")
            else:
                print(f"Item found: id={item_id}, name={item['name']}, price={item['price']}, quantity={item['quantity']}")

        elif option == UPDATE_OPTION:
            raw_id = prompt_input("Enter item id to update: ")
            item_id = validate_item_id(raw_id)
            if item_id is None:
                print("Error: invalid input")
                continue
            if item_id not in items:
                print("Item not found")
                continue
            # Ask which fields to update; empty input means keep current
            print("Press Enter without typing to keep current value.")
            raw_name = prompt_input(f"Enter new name (current: {items[item_id]['name']}): ")
            new_name = None
            if raw_name.strip() != "":
                validated_name = validate_name(raw_name)
                if validated_name is None:
                    print("Error: invalid input")
                    continue
                new_name = validated_name
            raw_price = prompt_input(f"Enter new price (current: {items[item_id]['price']}): ")
            new_price = None
            if raw_price.strip() != "":
                validated_price = validate_price(raw_price)
                if validated_price is None:
                    print("Error: invalid input")
                    continue
                new_price = validated_price
            raw_quantity = prompt_input(f"Enter new quantity (current: {items[item_id]['quantity']}): ")
            new_quantity = None
            if raw_quantity.strip() != "":
                validated_quantity = validate_quantity(raw_quantity)
                if validated_quantity is None:
                    print("Error: invalid input")
                    continue
                new_quantity = validated_quantity
            updated = update_item(items, item_id, new_name, new_price, new_quantity)
            if updated:
                print("Item updated")
            else:
                # Should not happen because we already checked existence
                print("Item not found")

        elif option == DELETE_OPTION:
            raw_id = prompt_input("Enter item id to delete: ")
            item_id = validate_item_id(raw_id)
            if item_id is None:
                print("Error: invalid input")
                continue
            deleted = delete_item(items, item_id)
            if deleted:
                print("Item deleted")
            else:
                print("Item not found")

        elif option == LIST_OPTION:
            entries = list_items(items)
            print("Items list:")
            if not entries:
                print("(no items)")
            else:
                for e in entries:
                    print(f"id={e[0]}, name={e[1]}, price={e[2]}, quantity={e[3]}")

# -------------------------
# Conclusions (5-8 lines) - placed here as comments
# -------------------------
# Conclusions:
# Using separate functions for each CRUD operation simplified the code by enforcing
# single responsibility: each function has a clear purpose and interface.
# The dict-based structure allowed efficient lookups and natural uniqueness of item ids,
# which simplifies create/read/update/delete semantics.
# Input validation is the most error-prone part; by centralizing validation helpers the code
# becomes easier to maintain and less likely to accept invalid values.
# To extend this CRUD into a larger system, persist the dict to a JSON file or use a database;
# also add user authentication, logging, and more advanced search/filter capabilities.

# -------------------------
# If this file is executed directly, run main()
# -------------------------
if __name__ == "__main__":
    main()

# End of file.
