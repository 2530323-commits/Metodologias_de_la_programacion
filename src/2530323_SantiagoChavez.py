# Student: Santiago Joshue Chavez Rivera
# Matriculation: 2530323        
# Group: IM 1-3
#
# Executive Summary:
# This document contains six Python programs that exercise string handling: creation,
# normalization, indexing, slicing, searching, replacing, splitting, joining and formatting.
# A string in Python is an immutable text sequence (type: str); operations return new strings.
# We will show how to validate and normalize user input (strip, lower/upper) and why that
# avoids errors when checking formats (emails, passwords, palindromes). Each problem
# includes a short description, input/output specification, validations, and three test cases.
#
# Principles and Best Practices:
# - Strings are immutable: any modification returns a new string.
# - Normalize input with strip() and lower() before comparisons.
# - Avoid magic numbers in slices; explain what each slice extracts in comments.
# - Prefer built-in string methods instead of reimplementing low-level logic.
# - Validate: (1) not empty after strip(), (2) format checks.
# - Use clear variable names in lower_snake_case and constants in UPPER_SNAKE_CASE.
#
# Template (placed before each problem as comments):
# Problem X: <short title>
# Description: 2-4 lines explaining what the program does.
#
# Inputs:
# - ...
#
# Outputs:
# - ...
#
# Validations:
# - ...
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...
#
# -----------------------------------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# Description: Normalize a full name, return Title Case name and initials (e.g. J.C.T.).
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - Not empty after strip()
# - Must contain at least two words
#
# Test cases:
# 1) Normal: "juan carlos tovar" -> Formatted name: "Juan Carlos Tovar", Initials: "J.C.T."
# 2) Border: " single" -> Error (only one word)
# 3) Error: "   " -> Error: invalid input

def format_full_name(full_name: str):
    full_name = full_name.strip()
    if not full_name:
        return (False, "Error: invalid input")
    # collapse multiple spaces between words
    parts = [p for p in full_name.split() if p]
    if len(parts) < 2:
        return (False, "Error: invalid input - must contain at least two words")
    # Title case each part
    formatted = " ".join(p.title() for p in parts)
    initials = ".".join(p[0].upper() for p in parts) + "."
    return (True, {"Formatted name": formatted, "Initials": initials})

# -----------------------------------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# Description: Basic structural validation: exactly one '@', at least one '.' after '@', no spaces.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true/false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - Not empty after strip()
# - Exactly one '@'
# - No spaces
#
# Test cases:
# 1) Normal: "user@example.com" -> Valid true, Domain: example.com
# 2) Border: "user@sub.domain.co" -> Valid true, Domain: sub.domain.co
# 3) Error: "user@@example.com" -> Valid false

def validate_email(email_text: str):
    email_text = email_text.strip()
    if not email_text:
        return (False, "Valid email: false", "Error: invalid input")
    if " " in email_text:
        return (False, "Valid email: false", "Error: contains spaces")
    at_count = email_text.count("@")
    if at_count != 1:
        return (False, "Valid email: false", "Error: must contain exactly one '@'")
    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]
    if "." not in domain_part:
        return (False, "Valid email: false", "Error: domain must contain '.'")
    return (True, "Valid email: true", f"Domain: {domain_part}")

# -----------------------------------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Determines whether a phrase is a palindrome ignoring spaces and case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true/false"
# - Optionally: "Normalized: <value>"
#
# Validations:
# - Not empty after strip()
# - Normalized length >= 3
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "aa" -> length after cleaning < 3 -> error/border
# 3) Error: "   " -> invalid input

def is_palindrome(phrase: str):
    phrase = phrase.strip()
    if not phrase:
        return (False, "Error: invalid input")
    # normalize: remove spaces and make lowercase
    normalized = "".join(ch.lower() for ch in phrase if ch != " ")
    if len(normalized) < 3:
        return (False, "Error: normalized string too short")
    is_pal = normalized == normalized[::-1]
    return (True, {"Is palindrome": str(is_pal).lower(), "Normalized": normalized})

# -----------------------------------------------------------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# Description: Given a sentence, show word count, first/last word, shortest and longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count, First word, Last word, Shortest word, Longest word
#
# Validations:
# - Not empty after strip()
# - At least one word after split()
#
# Test cases:
# 1) Normal: "This is a test sentence." -> words count 4 or 5 depending on punctuation handling
# 2) Border: "Hello" -> one word
# 3) Error: "   " -> invalid input

def sentence_word_stats(sentence: str):
    sentence = sentence.strip()
    if not sentence:
        return (False, "Error: invalid input")
    # split on whitespace — punctuation stays attached to words
    words = [w for w in sentence.split() if w]
    if not words:
        return (False, "Error: no valid words found")
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]
    # compute shortest and longest by length
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    return (True, {
        "Word count": word_count,
        "First word": first_word,
        "Last word": last_word,
        "Shortest word": shortest_word,
        "Longest word": longest_word
    })

# -----------------------------------------------------------------------------
# Problem 5: Password strength classifier
# Description: Classify password as weak, medium or strong using documented rules.
# Rules (documented):
# - Weak: length < 8 OR all letters are lowercase and no digits/symbols
# - Medium: length >= 8 and at least two of (has_upper, has_lower, has_digit)
# - Strong: length >= 8 and has_upper and has_lower and has_digit and has_symbol
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak/medium/strong"
#
# Validations:
# - Not empty
# - Length at least 1
#
# Test cases:
# 1) Normal: "P@ssw0rd" -> strong
# 2) Border: "password" -> weak (length 8 but all lowercase)
# 3) Error: "" -> invalid input

def classify_password_strength(password_input: str):
    if password_input is None:
        return (False, "Error: invalid input")
    password = password_input.strip()
    if not password:
        return (False, "Error: invalid input")
    length = len(password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(not ch.isalnum() for ch in password)
    if length < 8 or (not has_digit and not has_symbol and has_lower and not has_upper):
        return (True, "Password strength: weak")
    # strong: all required
    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        return (True, "Password strength: strong")
    # else medium if length >=8 and mixes at least two categories
    categories = sum([has_upper, has_lower, has_digit, has_symbol])
    if length >= 8 and categories >= 2:
        return (True, "Password strength: medium")
    # fallback
    return (True, "Password strength: weak")

# -----------------------------------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# Description: Build a single-line label exactly 30 characters long: "Product: <NAME> | Price: $<PRICE>"
# If shorter -> pad with spaces at end; if longer -> truncate to 30 chars.
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - "Label: '<30-char-label>'"
#
# Validations:
# - product_name not empty after strip()
# - price_value convertible to positive float
#
# Test cases:
# 1) Normal: product "Milk", price 1.5 -> Label with padding
# 2) Border: very long product name -> truncated to 30 chars
# 3) Error: price "abc" -> invalid input

def format_product_label(product_name: str, price_value):
    product_name = product_name.strip()
    if not product_name:
        return (False, "Error: invalid input - product name empty")
    # validate price
    try:
        price_num = float(price_value)
        if price_num < 0:
            return (False, "Error: price must be positive")
    except Exception:
        return (False, "Error: invalid price")
    label_base = f"Product: {product_name} | Price: ${price_num}"
    # ensure exactly 30 chars
    if len(label_base) > 30:
        label_fixed = label_base[:30]
    else:
        label_fixed = label_base.ljust(30)
    return (True, f"Label: '{label_fixed}'")

# -----------------------------------------------------------------------------
# Main: Run provided test cases for each problem and print results using required output phrasing.
# Note: Messages and variable names are in English per conventions.

if __name__ == "__main__":
    print("# Problem 1 tests")
    cases_p1 = [
        "juan carlos tovar",
        " single",
        "   "
    ]
    for c in cases_p1:
        ok, result = format_full_name(c)
        if not ok:
            print(result)
        else:
            print("Formatted name:", result["Formatted name"]) if isinstance(result, dict) else print(result)
            print("Initials:", result["Initials"]) if isinstance(result, dict) else None

    print('\n# Problem 2 tests')
    cases_p2 = [
        "user@example.com",
        "user@sub.domain.co",
        "user@@example.com"
    ]
    for c in cases_p2:
        ok, msg1, *rest = validate_email(c)
        print(msg1)
        if rest:
            print(rest[0])

    print('\n# Problem 3 tests')
    cases_p3 = [
        "Anita lava la tina",
        "aa",
        "   "
    ]
    for c in cases_p3:
        ok, result = is_palindrome(c)
        if not ok:
            print(result)
        else:
            print("Is palindrome:", result["Is palindrome"]) if isinstance(result, dict) else print(result)
            print("Normalized:", result["Normalized"]) if isinstance(result, dict) else None

    print('\n# Problem 4 tests')
    cases_p4 = [
        "This is a test sentence",
        "Hello",
        "   "
    ]
    for c in cases_p4:
        ok, result = sentence_word_stats(c)
        if not ok:
            print(result)
        else:
            print("Word count:", result["Word count"]) 
            print("First word:", result["First word"]) 
            print("Last word:", result["Last word"]) 
            print("Shortest word:", result["Shortest word"]) 
            print("Longest word:", result["Longest word"]) 

    print('\n# Problem 5 tests')
    cases_p5 = [
        "P@ssw0rd",
        "password",
        ""
    ]
    for c in cases_p5:
        ok, res = classify_password_strength(c)
        if not ok:
            print(res)
        else:
            print(res)

    print('\n# Problem 6 tests')
    cases_p6 = [
        ("Milk", 1.5),
        ("VeryLongProductNameThatExceedsThirtyCharacters", 12.99),
        ("Bread", "abc")
    ]
    for name, price in cases_p6:
        ok, res = format_product_label(name, price)
        if not ok:
            print(res)
        else:
            print(res)

# -----------------------------------------------------------------------------
# Conclusions (5-8 lines) - comments:
# Handling strings is essential for user input and output since most data comes as text.
# Use lower(), strip(), split() and join() to normalize, parse and reassemble strings reliably.
# Normalizing text before comparison prevents logic errors due to capitalization or extra spaces.
# Designing validations early (non-empty, format checks) prevents downstream errors and garbage data.
# Remember strings are immutable: use slices and methods that return new strings rather than modifying in-place.

# References:
# 1) Python documentation - Built-in Types: Text Sequence Type — str
# 2) Python tutorial - String methods (official docs)
# 3) "Automate the Boring Stuff with Python" - Chapter on strings
# 4) Real Python - Working with Strings in Python
# 5) Stack Overflow - various Q&A on string validation and parsing
